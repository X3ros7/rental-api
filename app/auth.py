"""@package app.auth
@brief JWT authentication helpers and current-user dependency.
"""

from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import settings
from app.database import get_db
from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(password: str) -> str:
    """@brief Hash a plain-text password with bcrypt.

    @param password Plain-text password.
    @return Bcrypt password hash.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """@brief Verify a plain-text password against a stored hash.

    @param plain_password Password provided by the user.
    @param hashed_password Stored bcrypt hash.
    @return ``True`` if the password matches, otherwise ``False``.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: str) -> str:
    """@brief Create a signed JWT access token.

    @param subject Token subject, typically the user email.
    @return Encoded JWT string.
    """
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def get_user_by_email(db: Session, email: str) -> User | None:
    """@brief Look up a user by email address.

    @param db Database session.
    @param email Email to search for.
    @return Matching ``User`` or ``None``.
    """
    return db.query(User).filter(User.email == email).first()


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    """@brief Authenticate a user by email and password.

    @param db Database session.
    @param email Login email.
    @param password Plain-text password.
    @return Authenticated ``User`` or ``None`` on failure.
    """
    user = get_user_by_email(db, email)
    if user is None or not verify_password(password, user.hashed_password):
        return None
    return user


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """@brief FastAPI dependency that resolves the current user from a Bearer JWT.

    @param token JWT from the ``Authorization: Bearer`` header.
    @param db Database session.
    @return Authenticated ``User``.
    @raises HTTPException 401 if the token is invalid or the user is missing.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email = payload.get("sub")
        if not isinstance(email, str) or not email:
            raise credentials_exception
    except JWTError as exc:
        raise credentials_exception from exc

    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user
