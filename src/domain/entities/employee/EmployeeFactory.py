from datetime import datetime
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.employee.value_objects.EmployeeStatus import EmployeeStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.shared.decorators.UtilityClass import utilityClass


@utilityClass
class EmployeeFactory:

    @staticmethod
    def create(
            userId: UserId,
            position: EmployeePosition,
            status: EmployeeStatus,
            salary: float,
            id: Optional[EmployeeId] = None,
            createAt: Optional[datetime] = None) -> Employee:
        return Employee(
            userId=userId,
            salary=DomainUtils.validateSalary(salary),
            position=DomainUtils.validateEnum(position, EmployeePosition),
            status=DomainUtils.validateEnum(status, EmployeeStatus),
            id=DomainUtils.resolveId(id, EmployeeId),
            createdAt=DomainUtils.resolveCreatedAt(createAt),
        )

    @staticmethod
    def update(
            employee: Employee,
            userId: Optional[UserId] = None,
            position: Optional[EmployeePosition] = None,
            status: Optional[EmployeeStatus] = None,
            salary: Optional[float] = None) -> Employee:
        return Employee(
            id=employee.getId(),
            userId=userId if userId is not None else employee.getUserId(),
            position=DomainUtils.validateEnum(position, EmployeePosition) if position is not None else employee.getPosition(),
            status=DomainUtils.validateEnum(status, EmployeeStatus) if status is not None else employee.getStatus(),
            salary=DomainUtils.validateSalary(salary) if salary is not None else employee.getSalary(),
            createdAt=employee.getCreatedAt()
        )
