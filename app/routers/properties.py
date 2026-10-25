"""@package app.routers.properties
@brief CRUD endpoints for rental properties, including list filters.
"""

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Property, User
from app.schemas import PropertyCreate, PropertyResponse, PropertyUpdate

router = APIRouter(prefix="/properties", tags=["properties"])


@router.get("", response_model=list[PropertyResponse])
def list_properties(
    city: str | None = Query(default=None),
    minPrice: float | None = Query(default=None, alias="minPrice", ge=0),
    maxPrice: float | None = Query(default=None, alias="maxPrice", ge=0),
    available: bool | None = Query(default=None),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> list[Property]:
    """@brief List properties with optional filters.

    Supported query parameters: ``city``, ``minPrice``, ``maxPrice``, ``available``.

    @param city Filter by city (case-insensitive exact match).
    @param minPrice Minimum monthly price (inclusive).
    @param maxPrice Maximum monthly price (inclusive).
    @param available Filter by availability flag.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return List of matching properties ordered by ID.
    """
    query = db.query(Property)

    if city is not None:
        query = query.filter(Property.city.ilike(city))
    if minPrice is not None:
        query = query.filter(Property.price_per_month >= minPrice)
    if maxPrice is not None:
        query = query.filter(Property.price_per_month <= maxPrice)
    if available is not None:
        query = query.filter(Property.available.is_(available))

    return query.order_by(Property.id).all()


@router.get("/{property_id}", response_model=PropertyResponse)
def get_property(
    property_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Property:
    """@brief Get a property by ID.

    @param property_id Property identifier.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Requested property.
    @raises HTTPException 404 if the property does not exist.
    """
    property_obj = db.get(Property, property_id)
    if property_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
    return property_obj


@router.post("", response_model=PropertyResponse, status_code=status.HTTP_201_CREATED)
def create_property(
    payload: PropertyCreate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Property:
    """@brief Create a new property listing.

    @param payload Property fields.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Created property.
    """
    property_obj = Property(
        title=payload.title,
        address=payload.address,
        city=payload.city,
        price_per_month=payload.pricePerMonth,
        bedrooms=payload.bedrooms,
        available=payload.available,
    )
    db.add(property_obj)
    db.commit()
    db.refresh(property_obj)
    return property_obj


@router.put("/{property_id}", response_model=PropertyResponse)
def update_property(
    property_id: int,
    payload: PropertyUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> Property:
    """@brief Fully replace an existing property.

    @param property_id Property identifier.
    @param payload New property fields.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @return Updated property.
    @raises HTTPException 404 if the property does not exist.
    """
    property_obj = db.get(Property, property_id)
    if property_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")

    property_obj.title = payload.title
    property_obj.address = payload.address
    property_obj.city = payload.city
    property_obj.price_per_month = payload.pricePerMonth
    property_obj.bedrooms = payload.bedrooms
    property_obj.available = payload.available

    db.commit()
    db.refresh(property_obj)
    return property_obj


@router.delete("/{property_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_property(
    property_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
) -> None:
    """@brief Delete a property and clear tenant assignments to it.

    @param property_id Property identifier.
    @param db Database session.
    @param _ Authenticated user (authorization only).
    @raises HTTPException 404 if the property does not exist.
    """
    property_obj = db.get(Property, property_id)
    if property_obj is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")

    for tenant in property_obj.tenants:
        tenant.property_id = None

    db.delete(property_obj)
    db.commit()
