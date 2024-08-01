from typing import Optional

from src.shared.error.DomainException import DomainException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.DomainErrorType import DomainErrorType
from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.EmployeeFactory import EmployeeFactory
from src.domain.entities.employee.ports.EmployeeGateway import EmployeeGateway
from src.domain.entities.employee.ports.EmployeeRepository import EmployeeRepository
from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.employee.value_objects.EmployeeStatus import EmployeeStatus
from src.domain.entities.user.value_objects.UserId import UserId


class EmployeeUseCase(EmployeeGateway):

    __employeeRepository: EmployeeRepository

    def __init__(self, employeeOutputAdapter: EmployeeRepository):
        self.__employeeRepository = employeeOutputAdapter

    def createEmployee(self,
                       userId: UserId,
                       position: EmployeePosition,
                       status: EmployeeStatus,
                       salary: float,
                       ) -> Employee:

        self.__validateUserId(userId)
        self.__validateNewEmployee(userId)

        newEmployee: Employee = EmployeeFactory.create(
            userId=userId,
            position=position,
            status=status,
            salary=salary
        )
        self.__employeeRepository.saveEmployee(newEmployee)
        return newEmployee

    def updateEmployee(self,
                       employeeId: EmployeeId,
                       userId: Optional[UserId] = None,
                       position: Optional[EmployeePosition] = None,
                       status: Optional[EmployeeStatus] = None,
                       salary: Optional[float] = None
                       ) -> Employee:

        employee: Optional[Employee] = self.__employeeRepository.findById(employeeId)

        updatedEmployee: Employee = EmployeeFactory.update(
            employee=employee,
            userId=userId,
            position=position,
            status=status,
            salary=salary
        )
        self.__employeeRepository.updateEmployee(updatedEmployee)
        return updatedEmployee

    def __validateNewEmployee(self, userId: UserId) -> Optional[Employee]:
        employee: Optional[Employee] = self.__employeeRepository.findByUserId(userId)
        if employee is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.EMPLOYEE_ALREADY_EXISTS
            ))
        return employee

    @staticmethod
    def __validateUserId(userId: UserId) -> None:
        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))
