from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.output_adapters.common.EntityIdAdapter import EntityIdAdapter


class VehicleData(DatabaseService.getBase()):

    __tablename__ = '_vehicle'

    id = Column(EntityIdAdapter(VehicleId), primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('_user.id'), nullable=False)
    license_plate = Column(String(7), nullable=False, unique=True)
    model = Column(String(50), nullable=False)
    vehicle_type = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
