from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.infrastructure.common.DatabaseService import DatabaseService


class CellData(DatabaseService.getBase()):

    __tablename__ = '_cell'

    id = Column(UUID(as_uuid=True), primary_key=True)
    space_number = Column(String(10), nullable=False, unique=True)
    vehicle_type = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
