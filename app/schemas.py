"""@package app.schemas
@brief Pydantic request/response schemas (JSON fields in camelCase).
"""

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Token(BaseModel):
    """@brief OAuth2 access token response.

    @var access_token JWT access token.
    @var token_type Token type, always ``bearer``.
    """

    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    """@brief Payload for user registration.

    @var email Unique email address.
    @var password Account password (min 6 characters).
    @var fullName Display name.
    """

    email: EmailStr
    password: str = Field(min_length=6)
    fullName: str = Field(alias="fullName", min_length=1)

    model_config = ConfigDict(populate_by_name=True)


class UserResponse(BaseModel):
    """@brief Public user representation.

    @var id User identifier.
    @var email User email.
    @var fullName Display name.
    """

    id: int
    email: EmailStr
    fullName: str = Field(validation_alias="full_name", serialization_alias="fullName")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class PropertyBase(BaseModel):
    """@brief Shared property fields for create/update payloads.

    @var title Listing title.
    @var address Street address.
    @var city City name.
    @var pricePerMonth Monthly rent.
    @var bedrooms Number of bedrooms.
    @var available Availability flag.
    """

    title: str = Field(min_length=1)
    address: str = Field(min_length=1)
    city: str = Field(min_length=1)
    pricePerMonth: float = Field(alias="pricePerMonth", gt=0)
    bedrooms: int = Field(ge=0)
    available: bool = True

    model_config = ConfigDict(populate_by_name=True)


class PropertyCreate(PropertyBase):
    """@brief Payload for creating a property."""

    pass


class PropertyUpdate(PropertyBase):
    """@brief Payload for fully replacing a property."""

    pass


class PropertyResponse(BaseModel):
    """@brief Property representation returned by the API.

    @var id Property identifier.
    @var title Listing title.
    @var address Street address.
    @var city City name.
    @var pricePerMonth Monthly rent.
    @var bedrooms Number of bedrooms.
    @var available Availability flag.
    """

    id: int
    title: str
    address: str
    city: str
    pricePerMonth: float = Field(validation_alias="price_per_month", serialization_alias="pricePerMonth")
    bedrooms: int
    available: bool

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class TenantBase(BaseModel):
    """@brief Shared tenant fields for create/update payloads.

    @var firstName Given name.
    @var lastName Family name.
    @var email Contact email.
    @var phone Phone number.
    @var propertyId Optional assigned property ID.
    """

    firstName: str = Field(alias="firstName", min_length=1)
    lastName: str = Field(alias="lastName", min_length=1)
    email: EmailStr
    phone: str = Field(min_length=1)
    propertyId: int | None = Field(default=None, alias="propertyId")

    model_config = ConfigDict(populate_by_name=True)


class TenantCreate(TenantBase):
    """@brief Payload for creating a tenant."""

    pass


class TenantUpdate(TenantBase):
    """@brief Payload for fully replacing a tenant."""

    pass


class TenantResponse(BaseModel):
    """@brief Tenant representation returned by the API.

    @var id Tenant identifier.
    @var firstName Given name.
    @var lastName Family name.
    @var email Contact email.
    @var phone Phone number.
    @var propertyId Assigned property ID, if any.
    """

    id: int
    firstName: str = Field(validation_alias="first_name", serialization_alias="firstName")
    lastName: str = Field(validation_alias="last_name", serialization_alias="lastName")
    email: EmailStr
    phone: str
    propertyId: int | None = Field(
        default=None,
        validation_alias="property_id",
        serialization_alias="propertyId",
    )

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class AssignPropertyRequest(BaseModel):
    """@brief Payload for assigning a property to a tenant.

    @var propertyId ID of the property to assign.
    """

    propertyId: int = Field(alias="propertyId")

    model_config = ConfigDict(populate_by_name=True)
