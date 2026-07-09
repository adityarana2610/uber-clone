import uuid
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.models.ride import RideStatus


class RideRequestCreate(BaseModel):
    pickup_lat: float
    pickup_lng: float
    dropoff_lat: float
    dropoff_lng: float


class RideResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    rider_id: uuid.UUID
    driver_id: uuid.UUID | None
    pickup_lat: float
    pickup_lng: float
    dropoff_lat: float
    dropoff_lng: float
    status: RideStatus
    requested_at: datetime
    accepted_at: datetime | None
    started_at: datetime | None
    completed_at: datetime | None
    cancelled_at: datetime | None