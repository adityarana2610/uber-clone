import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.models.user import User, UserRole
from app.models.driver import Driver
from app.models.rider import Rider
from app.core.security import hash_password

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        id=uuid.uuid4(),
        email=payload.email,
        hashed_password=hash_password(payload.password),
        full_name=payload.full_name,
        phone_number=payload.phone_number,
        role=payload.role,
    )
    db.add(new_user)

    try:
        db.flush()  # sends INSERT to DB, but doesn't commit yet — lets us catch errors before committing
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email or phone number already registered",
        )

    if payload.role == UserRole.DRIVER:
        db.add(Driver(user_id=new_user.id, vehicle_make="", vehicle_model="", plate_number=f"TEMP-{new_user.id}", license_number=f"TEMP-{new_user.id}"))
    else:
        db.add(Rider(user_id=new_user.id))

    db.commit()
    db.refresh(new_user)
    return new_user