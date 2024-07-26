from abc import ABC, abstractmethod

from src.domain.entities.employee.Employee import Employee


class EmployeeRepository(ABC):

    @abstractmethod
    def saveEmployee(self, employee: Employee) -> Employee:
        pass
