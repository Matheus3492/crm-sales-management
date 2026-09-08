from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:
    def create(self, db: Session, customer: Customer) -> Customer:
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    def get_by_id(self, db: Session, customer_id: int) -> Customer | None:
        return db.get(Customer, customer_id)

    def get_by_email(self, db: Session, email: str) -> Customer | None:
        statement = select(Customer).where(Customer.email == email)
        return db.scalar(statement)

    def get_all(self, db: Session) -> list[Customer]:
        statement = select(Customer).order_by(Customer.id)
        return list(db.scalars(statement).all())