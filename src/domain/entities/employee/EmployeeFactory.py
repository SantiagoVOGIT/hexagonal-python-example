from datetime import datetime
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.value_objects.UserId import UserId
from src.shared.decorators.UtilityClass import utilityClass


@utilityClass
class EmployeeFactory:

    @staticmethod
    def create(
               userId: UserId,
               position: EmployeePosition,
               salary: float,
               hireDate: datetime,
               id: Optional[EmployeeId] = None,
               createAt: Optional[datetime] = None) -> Employee:

        return Employee(
            userId=userId,
            hireDate=hireDate,
            salary=DomainUtils.validateSalary(salary),
            position=DomainUtils.validateEnum(position, EmployeePosition),
            id=DomainUtils.resolveId(id, EmployeeId),
            createdAt=DomainUtils.resolveCreatedAt(createAt),
        )
