from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.output_adapters.persistence.entities.EntityIdAdapter import EntityIdAdapter


class ReservationData(DatabaseService.getBase()):

    __tablename__ = '_reservation'

    id = Column(EntityIdAdapter(ReservationId), primary_key=True)
    user_id = Column(EntityIdAdapter(UserId), ForeignKey('_user.id'), nullable=False)
    cell_id = Column(EntityIdAdapter(CellId), ForeignKey('_cell.id'), nullable=False)
    vehicle_id = Column(EntityIdAdapter(VehicleId), ForeignKey('_vehicle.id'), nullable=False)
    reservation_code = Column(String(10), unique=True)
    status = Column(String(20), nullable=False)
    start_time = Column(DateTime(timezone=True))
    end_time = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), nullable=False)
