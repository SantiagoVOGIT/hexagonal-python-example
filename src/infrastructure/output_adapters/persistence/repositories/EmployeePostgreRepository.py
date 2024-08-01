from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.ports.EmployeeRepository import EmployeeRepository
from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.user.value_objects.UserId import UserId
from src.infrastructure.common.DatabaseService import DatabaseService
from src.shared.error.CustomException import CustomException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.ErrorType import ErrorType
from src.shared.error.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.employee_data.EmployeeData import EmployeeData
from src.infrastructure.output_adapters.persistence.entities.employee_data.EmployeeMapper import EmployeeMapper


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

    def findById(self, employeeId: EmployeeId) -> Optional[Employee]:
        session: Session = self.__databaseService.getSession()
        try:
            employeeData: Optional[EmployeeData] = session.query(EmployeeData).filter(
                EmployeeData.id == employeeId.getValue()
            ).first()

            if employeeData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.INFRASTRUCTURE_ERROR,
                    InfrastructureErrorType.EMPLOYEE_NOT_FOUND.name,
                    InfrastructureErrorType.EMPLOYEE_NOT_FOUND.value
                ))
            return EmployeeMapper.toDomain(employeeData)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def updateEmployee(self, employee: Employee) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            employeeData = session.query(EmployeeData).filter(
                EmployeeData.id == employee.getId().getValue()
            ).first()

            employeeData.user_id = employee.getUserId().getValue()
            employeeData.position = employee.getPosition().getValue()
            employeeData.status = employee.getStatus().getValue()
            employeeData.salary = employee.getSalary()

            session.commit()
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

    def findByUserId(self, userId: UserId) -> Optional[Employee]:
        session: Session = self.__databaseService.getSession()
        try:
            employeeData: Optional[EmployeeData] = session.query(EmployeeData).filter(
                EmployeeData.user_id == userId.getValue()
            ).first()
            if employeeData is None:
                return None
            return EmployeeMapper.toDomain(employeeData)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()
