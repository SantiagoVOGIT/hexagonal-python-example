from abc import ABC, abstractmethod
from typing import Optional, List

from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.user.value_objects.UserId import UserId


class EmployeeRepository(ABC):

    @abstractmethod
    def saveEmployee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def updateEmployee(self, employee: Employee) -> None:
        pass

    @abstractmethod
    def findById(self, employeeId: EmployeeId) -> Optional[Employee]:
        pass

    @abstractmethod
    def findByUserId(self, userId: UserId) -> Optional[Employee]:
        pass

    @abstractmethod
    def getAllEmployees(self) -> List[Employee]:
        pass
