from fastapi import APIRouter, HTTPException, status

from app.schemas import User, UserCreate
from app.services.users import DuplicateEmailError, user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate) -> User:
    try:
        return user_service.create_user(payload)
    except DuplicateEmailError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        ) from None
