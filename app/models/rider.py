from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Rider(Base):
    __tablename__ = "riders"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), primary_key=True)
    payment_method_ref = Column(String, nullable=True)
    rating = Column(Float, nullable=False, default=5.0)