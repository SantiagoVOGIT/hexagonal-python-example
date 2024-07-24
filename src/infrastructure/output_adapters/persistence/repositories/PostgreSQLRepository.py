from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.common.utils.ErrorHandler import ExceptionHandler, CustomException, ErrorType
from src.domain.entities.user.User import User
from src.domain.output_ports.UserRepository import UserRepository
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.common.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.user_data.UserMapper import UserMapper
from src.infrastructure.output_adapters.persistence.entities.user_data.UserModel import UserModel


class PostgreSQLRepository(UserRepository):

    __databaseService: DatabaseService

    def __init__(self, adapterService: DatabaseService):
        self.__databaseService = adapterService

    def saveUser(self, user: User) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            userModel: UserModel = UserMapper.toPersistence(user)
            session.add(userModel)
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

    def findByEmail(self, emailAddress: str) -> Optional[User]:
        session: Session = self.__databaseService.getSession()
        try:
            userModel: Optional[UserModel] = session.query(UserModel).filter_by(email_address=emailAddress).first()
            if userModel is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.INFRASTRUCTURE_ERROR,
                    InfrastructureErrorType.USER_NOT_FOUND.name,
                    InfrastructureErrorType.USER_NOT_FOUND.value,
                    {"email": emailAddress}
                ))
            return UserMapper.toDomain(userModel)

        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def findByDniNumber(self, dniNumber: str) -> Optional[User]:
        session: Session = self.__databaseService.getSession()
        try:
            userModel: Optional[UserModel] = session.query(UserModel).filter_by(dni_number=dniNumber).first()
            if userModel is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.INFRASTRUCTURE_ERROR,
                    InfrastructureErrorType.USER_NOT_FOUND.name,
                    InfrastructureErrorType.USER_NOT_FOUND.value,
                    {"dni_number": dniNumber}
                ))
            return UserMapper.toDomain(userModel)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()
