"""@package app.routers.auth
@brief Authentication endpoints: register, login, and current user.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth import authenticate_user, create_access_token, get_current_user, get_user_by_email, hash_password
from app.database import get_db
from app.models import User
from app.schemas import Token, UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)) -> User:
    """@brief Register a new user account.

    @param payload Registration data (email, password, fullName).
    @param db Database session.
    @return Created user.
    @raises HTTPException 409 if the email is already registered.
    """
    if get_user_by_email(db, payload.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = User(
        email=payload.email,
        hashed_password=hash_password(payload.password),
        full_name=payload.fullName,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Token:
    """@brief Authenticate a user and issue a Bearer JWT.

    The OAuth2 form field ``username`` must contain the user email.

    @param form_data OAuth2 password form (username=email, password).
    @param db Database session.
    @return Access token payload.
    @raises HTTPException 401 if credentials are invalid.
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return Token(access_token=create_access_token(user.email))


@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)) -> User:
    """@brief Return the currently authenticated user.

    @param current_user User resolved from the Bearer JWT.
    @return Current user profile.
    """
    return current_user
