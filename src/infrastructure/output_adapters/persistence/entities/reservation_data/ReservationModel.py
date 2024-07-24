from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from src.infrastructure.common.DatabaseService import DatabaseService


class ReservationModel(DatabaseService.getBase()):

    __tablename__ = '_reservation'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('_user.id'), nullable=False)
    cell_id = Column(UUID(as_uuid=True), ForeignKey('_cell.id'), nullable=False)
    vehicle_id = Column(UUID(as_uuid=True), ForeignKey('_vehicle.id'), nullable=False)
    reservation_code = Column(String(10), unique=True)
    status = Column(String(20), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), nullable=False)
