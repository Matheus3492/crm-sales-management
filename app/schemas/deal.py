from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class DealCreate(BaseModel):
    title: str
    value: Decimal
    status: str = "new"
    customer_id: int
    user_id: int


class DealResponse(BaseModel):
    id: int
    title: str
    value: Decimal
    status: str
    customer_id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)