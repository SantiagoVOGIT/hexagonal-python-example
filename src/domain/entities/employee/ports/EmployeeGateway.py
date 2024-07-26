from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeVar

from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.value_objects.UserId import UserId

T = TypeVar('T')


class EmployeeGateway(ABC):

    @abstractmethod
    def createEmployee(self,
                       userId: UserId,
                       position: EmployeePosition,
                       salary: float,
                       hireDate: datetime) -> Employee:
        pass


