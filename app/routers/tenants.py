"""@package app.routers.tenants
@brief CRUD endpoints for tenants, plus property assign/unassign.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Property, Tenant, User
from app.schemas import AssignPropertyRequest, TenantCreate, TenantResponse, TenantUpdate

router = APIRouter(prefix="/tenants", tags=["tenants"])


def _ensure_property_exists(db: Session, property_id: int | None) -> None:
    """@brief Validate that a property ID exists when it is provided.

    @param db Database session.
    @param property_id Optional property identifier.
    @raises HTTPException 404 if ``property_id`` is set but not found.
    """
    if property_id is None:
        return
    if db.get(Property, property_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")


@router.get("", response_model=list[TenantResponse])
def list_tenants(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> list[Tenant]:
    """@brief List all tenants.

    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Tenants ordered by ID.
    """
    return db.query(Tenant).order_by(Tenant.id).all()


@router.get("/{tenant_id}", response_model=TenantResponse)
def get_tenant(
    tenant_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Tenant:
    """@brief Get a tenant by ID.

    @param tenant_id Tenant identifier.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Requested tenant.
    @raises HTTPException 404 if the tenant does not exist.
    """
    tenant = db.get(Tenant, tenant_id)
    if tenant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")
    return tenant


@router.post("", response_model=TenantResponse, status_code=status.HTTP_201_CREATED)
def create_tenant(
    payload: TenantCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Tenant:
    """@brief Create a new tenant.

    @param payload Tenant fields.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Created tenant.
    @raises HTTPException 409 if the email is already used.
    @raises HTTPException 404 if ``propertyId`` does not exist.
    """
    existing = db.query(Tenant).filter(Tenant.email == payload.email).first()
    if existing is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    _ensure_property_exists(db, payload.propertyId)

    tenant = Tenant(
        first_name=payload.firstName,
        last_name=payload.lastName,
        email=payload.email,
        phone=payload.phone,
        property_id=payload.propertyId,
    )
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant


@router.put("/{tenant_id}", response_model=TenantResponse)
def update_tenant(
    tenant_id: int,
    payload: TenantUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Tenant:
    """@brief Fully replace an existing tenant.

    @param tenant_id Tenant identifier.
    @param payload New tenant fields.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Updated tenant.
    @raises HTTPException 404 if the tenant or property does not exist.
    @raises HTTPException 409 if the email belongs to another tenant.
    """
    tenant = db.get(Tenant, tenant_id)
    if tenant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")

    existing = db.query(Tenant).filter(Tenant.email == payload.email, Tenant.id != tenant_id).first()
    if existing is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    _ensure_property_exists(db, payload.propertyId)

    tenant.first_name = payload.firstName
    tenant.last_name = payload.lastName
    tenant.email = payload.email
    tenant.phone = payload.phone
    tenant.property_id = payload.propertyId

    db.commit()
    db.refresh(tenant)
    return tenant


@router.delete("/{tenant_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tenant(
    tenant_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> None:
    """@brief Delete a tenant.

    @param tenant_id Tenant identifier.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @raises HTTPException 404 if the tenant does not exist.
    """
    tenant = db.get(Tenant, tenant_id)
    if tenant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")

    db.delete(tenant)
    db.commit()


@router.post("/{tenant_id}/assign", response_model=TenantResponse)
def assign_property(
    tenant_id: int,
    payload: AssignPropertyRequest,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Tenant:
    """@brief Assign an available property to a tenant.

    Marks the property as unavailable after a successful assignment.

    @param tenant_id Tenant identifier.
    @param payload Object containing ``propertyId``.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Updated tenant with assigned property.
    @raises HTTPException 404 if tenant or property is missing.
    @raises HTTPException 409 if the property is not available.
    """
    tenant = db.get(Tenant, tenant_id)
    if tenant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")

    property_obj = db.get(Property, payload.propertyId)
    if property_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    if not property_obj.available:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Property is not available")

    tenant.property_id = property_obj.id
    property_obj.available = False

    db.commit()
    db.refresh(tenant)
    return tenant


@router.post("/{tenant_id}/unassign", response_model=TenantResponse)
def unassign_property(
    tenant_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Tenant:
    """@brief Remove the property assignment from a tenant.

    If a property was assigned, it becomes available again.

    @param tenant_id Tenant identifier.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Updated tenant without a property assignment.
    @raises HTTPException 404 if the tenant does not exist.
    """
    tenant = db.get(Tenant, tenant_id)
    if tenant is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tenant not found")

    if tenant.property_id is not None:
        property_obj = db.get(Property, tenant.property_id)
        if property_obj is not None:
            property_obj.available = True
        tenant.property_id = None

    db.commit()
    db.refresh(tenant)
    return tenant
