import uuid
import enum
from datetime import datetime

from sqlalchemy import Column, String, Float, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class RideStatus(str, enum.Enum):
    REQUESTED = "requested"
    ACCEPTED = "accepted"
    ONGOING = "ongoing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class CancelledBy(str, enum.Enum):
    RIDER = "rider"
    DRIVER = "driver"


class Ride(Base):
    __tablename__ = "rides"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    rider_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    driver_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    pickup_lat = Column(Float, nullable=False)
    pickup_lng = Column(Float, nullable=False)
    dropoff_lat = Column(Float, nullable=False)
    dropoff_lng = Column(Float, nullable=False)

    status = Column(Enum(RideStatus), nullable=False, default=RideStatus.REQUESTED)

    cancelled_by = Column(Enum(CancelledBy), nullable=True)
    cancellation_reason = Column(String, nullable=True)

    requested_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    accepted_at = Column(DateTime, nullable=True)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    cancelled_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)