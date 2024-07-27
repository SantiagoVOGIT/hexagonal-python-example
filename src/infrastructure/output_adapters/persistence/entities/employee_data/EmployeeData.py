from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from src.infrastructure.common.DatabaseService import DatabaseService


class EmployeeData(DatabaseService.getBase()):

    __tablename__ = '_employee'

    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('_user.id'), nullable=False)
    position = Column(String(20), nullable=False)
    salary = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
