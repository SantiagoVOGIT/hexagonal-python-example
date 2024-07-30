from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.user.value_objects.UserId import UserId
from src.shared.utils.ErrorHandler import ExceptionHandler, CustomException, ErrorType
from src.domain.entities.user.User import User
from src.domain.entities.user.ports.UserRepository import UserRepository
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.common.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.user_data.UserMapper import UserMapper
from src.infrastructure.output_adapters.persistence.entities.user_data.UserData import UserData


class UserPostgreRepository(UserRepository):

    __databaseService: DatabaseService

    def __init__(self, adapterService: DatabaseService):
        self.__databaseService = adapterService

    def saveUser(self, user: User) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            userData: UserData = UserMapper.toPersistence(user)
            session.add(userData)
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

    def findByDniNumber(self, dniNumber: str) -> Optional[User]:
        session: Session = self.__databaseService.getSession()
        try:
            userData: Optional[UserData] = session.query(UserData).filter_by(
                dni_number=dniNumber
            ).first()
            if userData is None:
                return None
            return UserMapper.toDomain(userData)
        except SQLAlchemyError as exc:
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
            emailAddressData: Optional[UserData] = session.query(UserData).filter_by(
                email_address=emailAddress
            ).first()
            if emailAddressData is None:
                return None
            return UserMapper.toDomain(emailAddressData)

        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def findById(self, userId: UserId) -> Optional[User]:
        session: Session = self.__databaseService.getSession()
        try:
            userIdData: Optional[UserData] = session.query(UserData).filter_by(
                id=userId.getValue()
            ).first()
            if userIdData is None:
                return None
            return UserMapper.toDomain(userIdData)

        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()
