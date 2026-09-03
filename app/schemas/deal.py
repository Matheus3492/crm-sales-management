from decimal import Decimal

from pydantic import BaseModel


class DealCreate(BaseModel):
    title: str
    value: Decimal
    status: str = "new"
    customer_id: int
    user_id: int