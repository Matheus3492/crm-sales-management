from app.core.database import Base, engine
from app.models import Customer, Deal, User


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()