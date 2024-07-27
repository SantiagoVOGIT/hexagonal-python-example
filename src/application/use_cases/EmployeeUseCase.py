from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.EmployeeFactory import EmployeeFactory
from src.domain.entities.employee.ports.EmployeeRepository import EmployeeRepository
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.input_ports.EmployeeGateway import EmployeeGateway


class EmployeeUseCase(EmployeeGateway):

    __employeeRepository: EmployeeRepository

    def __init__(self, outputAdapter: EmployeeRepository):
        self.__employeeRepository = outputAdapter

    def createEmployee(self,
                       userId: UserId,
                       position: EmployeePosition,
                       salary: float,
                       ) -> Employee:

        newEmployee: Employee = EmployeeFactory.create(
            userId=userId,
            position=position,
            salary=salary,
        )
        self.__employeeRepository.saveEmployee(newEmployee)
        return newEmployee
