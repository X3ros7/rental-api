from sqlalchemy import Boolean, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)


class Property(Base):
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
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    property_id: Mapped[int | None] = mapped_column(ForeignKey("properties.id"), nullable=True)

    property: Mapped[Property | None] = relationship(back_populates="tenants")
