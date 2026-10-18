from sqlalchemy.orm import Session

from app.auth import get_user_by_email, hash_password
from app.models import Property, Tenant, User


def seed_demo_data(db: Session) -> None:
    if get_user_by_email(db, "admin@rentai.local") is None:
        db.add(
            User(
                email="admin@rentai.local",
                hashed_password=hash_password("admin123"),
                full_name="Admin User",
            )
        )

    if db.query(Property).count() == 0:
        properties = [
            Property(
                title="Sunny Downtown Studio",
                address="12 Main St",
                city="Berlin",
                price_per_month=950.0,
                bedrooms=0,
                available=True,
            ),
            Property(
                title="Family Apartment Near Park",
                address="45 Green Ave",
                city="Munich",
                price_per_month=1800.0,
                bedrooms=3,
                available=True,
            ),
            Property(
                title="River View Loft",
                address="8 Harbor Rd",
                city="Hamburg",
                price_per_month=1400.0,
                bedrooms=2,
                available=False,
            ),
        ]
        db.add_all(properties)
        db.flush()

        db.add_all(
            [
                Tenant(
                    first_name="Anna",
                    last_name="Schmidt",
                    email="anna.schmidt@example.com",
                    phone="+49111111111",
                    property_id=properties[2].id,
                ),
                Tenant(
                    first_name="Marco",
                    last_name="Rossi",
                    email="marco.rossi@example.com",
                    phone="+49222222222",
                    property_id=None,
                ),
            ]
        )

    db.commit()
