from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from src.infrastructure.common.DatabaseService import DatabaseService


class UserModel(DatabaseService.base):

    __tablename__ = '_user'

    id = Column(UUID, primary_key=True)
    dni_number = Column(String(10), nullable=False, unique=True)
    dni_type = Column(String(30), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(10))
    email_address = Column(String(70), unique=True)
    role = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
