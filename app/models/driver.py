import enum
from sqlalchemy import Column, String, Float, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class DriverStatus(str, enum.Enum):
    OFFLINE = "offline"
    ONLINE = "online"
    ON_TRIP = "on_trip"


class Driver(Base):
    __tablename__ = "drivers"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    vehicle_make = Column(String, nullable=False)
    vehicle_model = Column(String, nullable=False)
    plate_number = Column(String, unique=True, nullable=False)
    license_number = Column(String, unique=True, nullable=False)
    status = Column(Enum(DriverStatus), nullable=False, default=DriverStatus.OFFLINE)
    rating = Column(Float, nullable=False, default=5.0)