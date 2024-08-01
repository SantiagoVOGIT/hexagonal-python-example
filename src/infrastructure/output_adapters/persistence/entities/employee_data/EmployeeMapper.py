from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.employee.value_objects.EmployeeStatus import EmployeeStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.infrastructure.output_adapters.persistence.entities.employee_data.EmployeeData import EmployeeData


class EmployeeMapper:

    @staticmethod
    def toDomain(employeeData: EmployeeData) -> Employee:
        return Employee(
            id=EmployeeId(employeeData.id),
            userId=UserId(employeeData.user_id),
            position=EmployeePosition(employeeData.position),
            status=EmployeeStatus(employeeData.status),
            salary=employeeData.salary,
            createdAt=employeeData.created_at
        )

    @staticmethod
    def toPersistence(employee: Employee) -> EmployeeData:
        return EmployeeData(
            id=employee.getId().getValue(),
            user_id=employee.getUserId().getValue(),
            position=employee.getPosition().getValue(),
            status=employee.getStatus().getValue(),
            salary=employee.getSalary(),
            created_at=employee.getCreatedAt()
        )
