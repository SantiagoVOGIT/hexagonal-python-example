from sqlalchemy import Column, String, DateTime

from src.domain.entities.cell.value_objects.CellId import CellId
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.output_adapters.persistence.entities.EntityIdAdapter import EntityIdAdapter


class CellData(DatabaseService.getBase()):

    __tablename__ = '_cell'

    id = Column(EntityIdAdapter(CellId), primary_key=True)
    space_number = Column(String(10), nullable=False, unique=True)
    vehicle_type = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
