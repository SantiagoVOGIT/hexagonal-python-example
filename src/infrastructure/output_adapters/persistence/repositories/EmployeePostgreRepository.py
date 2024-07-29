from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.ports.EmployeeRepository import EmployeeRepository
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.common.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.employee_data.EmployeeData import EmployeeData
from src.infrastructure.output_adapters.persistence.entities.employee_data.EmployeeMapper import EmployeeMapper
from src.shared.utils.ErrorHandler import ExceptionHandler, CustomException, ErrorType


class EmployeePostgreRepository(EmployeeRepository):

    __databaseService: DatabaseService

    def __init__(self, adapterService: DatabaseService):
        self.__databaseService = adapterService

    def saveEmployee(self, employee: Employee) -> Employee:
        session: Session = self.__databaseService.getSession()
        try:
            employeeData: EmployeeData = EmployeeMapper.toPersistence(employee)
            session.add(employeeData)
            session.commit()
            return employee
        except SQLAlchemyError as exc:
            session.rollback()
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

