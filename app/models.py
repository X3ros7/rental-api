"""@package app.models
@brief SQLAlchemy ORM models: User, Property, and Tenant.
"""

from sqlalchemy import Boolean, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    """@brief Registered API user used for JWT authentication.

    @var id Unique identifier.
    @var email Unique login email.
    @var hashed_password Bcrypt password hash.
    @var full_name Display name of the user.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)


class Property(Base):
    """@brief Rental property listing.

    @var id Unique identifier.
    @var title Listing title.
    @var address Street address.
    @var city City name.
    @var price_per_month Monthly rent amount.
    @var bedrooms Number of bedrooms.
    @var available Whether the property is available for rent.
    @var tenants Related tenant records.
    """

    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    city: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    price_per_month: Mapped[float] = mapped_column(Float, nullable=False, index=True)
    bedrooms: Mapped[int] = mapped_column(Integer, nullable=False)
    available: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, index=True)

    tenants: Mapped[list["Tenant"]] = relationship(back_populates="property")


class Tenant(Base):
    """@brief Tenant (renter) entity.

    @var id Unique identifier.
    @var first_name Given name.
    @var last_name Family name.
    @var email Unique contact email.
    @var phone Phone number.
    @var property_id Optional FK to the assigned property.
    @var property Related property entity, if assigned.
    """

    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    property_id: Mapped[int | None] = mapped_column(ForeignKey("properties.id"), nullable=True)

    property: Mapped[Property | None] = relationship(back_populates="tenants")
