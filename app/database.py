"""@package app.database
@brief SQLAlchemy engine, session factory, and declarative base.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.config import settings

connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """@brief Declarative base class for all ORM models."""

    pass


def get_db() -> Generator[Session, None, None]:
    """@brief FastAPI dependency that yields a database session.

    The session is always closed after the request finishes.

    @return Generator yielding a SQLAlchemy ``Session``.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
