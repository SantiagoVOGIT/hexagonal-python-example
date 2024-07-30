from abc import ABC, abstractmethod
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
                       ) -> Employee:
        pass
