from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Property, Tenant, User
from app.schemas import AssignPropertyRequest, TenantCreate, TenantResponse, TenantUpdate

router = APIRouter(prefix="/tenants", tags=["tenants"])


def _ensure_property_exists(db: Session, property_id: int | None) -> None:
    if property_id is None:
        return
    if db.get(Property, property_id) is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")


@router.get("", response_model=list[TenantResponse])
def list_tenants(
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> list[Tenant]:
    return db.query(Tenant).order_by(Tenant.id).all()


@router.get("/{tenant_id}", response_model=TenantResponse)
def get_tenant(
    tenant_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Tenant:
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
