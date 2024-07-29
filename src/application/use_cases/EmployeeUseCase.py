from typing import Optional
from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.EmployeeFactory import EmployeeFactory
from src.domain.entities.employee.ports.EmployeeRepository import EmployeeRepository
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.ports.UserRepository import UserRepository
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.input_ports.EmployeeGateway import EmployeeGateway
from src.shared.utils.ErrorHandler import ExceptionHandler, DomainException


class EmployeeUseCase(EmployeeGateway):

    __employeeRepository: EmployeeRepository
    __userRepository: UserRepository

    def __init__(self,
                 employeeOutputAdapter: EmployeeRepository,
                 userOutputAdapter: UserRepository
                 ):
        self.__employeeRepository = employeeOutputAdapter
        self.__userRepository = userOutputAdapter

    def createEmployee(self,
                       userId: UserId,
                       position: EmployeePosition,
                       salary: float,
                       ) -> Employee:

        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))

        existingEmployee: Optional[Employee] = self.__userRepository.findById(userId)
        if existingEmployee is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.EMPLOYEE_ALREADY_EXISTS,
                {"userId": userId}
            ))

        newEmployee: Employee = EmployeeFactory.create(
            userId=userId,
            position=position,
            salary=salary,
        )
        self.__employeeRepository.saveEmployee(newEmployee)
        return newEmployee
