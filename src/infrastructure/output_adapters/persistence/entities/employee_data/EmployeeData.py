from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey

from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.user.value_objects.UserId import UserId
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.output_adapters.persistence.entities.EntityIdAdapter import EntityIdAdapter


class EmployeeData(DatabaseService.getBase()):

    __tablename__ = '_employee'

    id = Column(EntityIdAdapter(EmployeeId), primary_key=True)
    user_id = Column(EntityIdAdapter(UserId), ForeignKey('_user.id'), nullable=False)
    position = Column(String(20), nullable=False)
    salary = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)
