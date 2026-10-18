from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    fullName: str = Field(alias="fullName", min_length=1)

    model_config = ConfigDict(populate_by_name=True)


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    fullName: str = Field(validation_alias="full_name", serialization_alias="fullName")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class PropertyBase(BaseModel):
    title: str = Field(min_length=1)
    address: str = Field(min_length=1)
    city: str = Field(min_length=1)
    pricePerMonth: float = Field(alias="pricePerMonth", gt=0)
    bedrooms: int = Field(ge=0)
    available: bool = True

    model_config = ConfigDict(populate_by_name=True)


class PropertyCreate(PropertyBase):
    pass


class PropertyUpdate(PropertyBase):
    pass


class PropertyResponse(BaseModel):
    id: int
    title: str
    address: str
    city: str
    pricePerMonth: float = Field(validation_alias="price_per_month", serialization_alias="pricePerMonth")
    bedrooms: int
    available: bool

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class TenantBase(BaseModel):
    firstName: str = Field(alias="firstName", min_length=1)
    lastName: str = Field(alias="lastName", min_length=1)
    email: EmailStr
    phone: str = Field(min_length=1)
    propertyId: int | None = Field(default=None, alias="propertyId")

    model_config = ConfigDict(populate_by_name=True)


class TenantCreate(TenantBase):
    pass


class TenantUpdate(TenantBase):
    pass


class TenantResponse(BaseModel):
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
    propertyId: int = Field(alias="propertyId")

    model_config = ConfigDict(populate_by_name=True)
