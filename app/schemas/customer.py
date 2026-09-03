from pydantic import BaseModel, ConfigDict, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    phone: str | None = None


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr | None = None
    phone: str | None = None

    model_config = ConfigDict(from_attributes=True)