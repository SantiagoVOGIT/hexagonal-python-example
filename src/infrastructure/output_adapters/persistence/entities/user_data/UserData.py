from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from src.infrastructure.common.DatabaseService import DatabaseService


class UserData(DatabaseService.getBase()):

    __tablename__ = '_user'

    id = Column(UUID(as_uuid=True), primary_key=True)
    dni_number = Column(String(10), nullable=False, unique=True)
    dni_type = Column(String(30), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(10))
    email_address = Column(String(70), nullable=False, unique=True)
    role = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
