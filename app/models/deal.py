from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Deal(Base):
    __tablename__ = "deals"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    value: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="open",
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.id"),
        nullable=False,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )