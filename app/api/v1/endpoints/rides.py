import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.schemas.ride import RideRequestCreate, RideResponse
from app.models.ride import Ride, RideStatus
from app.models.ride_status_history import RideStatusHistory
from app.models.user import User, UserRole

router = APIRouter()


@router.post("/request", response_model=RideResponse, status_code=status.HTTP_201_CREATED)
def request_ride(
    payload: RideRequestCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if current_user.role != UserRole.RIDER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only riders can request rides",
        )

    active_ride = (
        db.query(Ride)
        .filter(
            Ride.rider_id == current_user.id,
            Ride.status.in_([RideStatus.REQUESTED, RideStatus.ACCEPTED, RideStatus.ONGOING]),
        )
        .first()
    )
    if active_ride:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="You already have an active ride in progress",
        )

    new_ride = Ride(
        id=uuid.uuid4(),
        rider_id=current_user.id,
        pickup_lat=payload.pickup_lat,
        pickup_lng=payload.pickup_lng,
        dropoff_lat=payload.dropoff_lat,
        dropoff_lng=payload.dropoff_lng,
        status=RideStatus.REQUESTED,
    )
    db.add(new_ride)
    db.flush()  # get new_ride.id populated, and surface any DB errors early

    history_entry = RideStatusHistory(
        id=uuid.uuid4(),
        ride_id=new_ride.id,
        status=RideStatus.REQUESTED,
        changed_by=current_user.id,
    )
    db.add(history_entry)

    db.commit()
    db.refresh(new_ride)
    return new_ride