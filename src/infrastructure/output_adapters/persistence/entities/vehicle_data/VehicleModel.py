from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.infrastructure.common.DatabaseService import DatabaseService


class VehicleModel(DatabaseService.base):

    __tablename__ = '_vehicle'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('_user.id'), nullable=False)
    license_plate = Column(String(7), nullable=False, unique=True)
    model = Column(String(50), nullable=False)
    vehicle_type = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
