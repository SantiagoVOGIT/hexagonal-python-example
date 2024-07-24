from typing import Optional

from sqlalchemy.orm import Session

from src.domain.entities.user.User import User
from src.domain.output_ports.UserRepository import UserRepository
from src.infrastructure.common.DatabaseService import DatabaseService
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
        except Exception as exc:
            session.rollback()
            raise exc
        finally:
            session.close()

    def findByEmail(self, emailAddress: str) -> Optional[User]:
        session: Session = self.__databaseService.getSession()
        try:
            userModel: Optional[UserModel] = session.query(UserModel).filter_by(email_address=emailAddress).first()
            return UserMapper.toDomain(userModel) if userModel is not None else None
        finally:
            session.close()

    def findByDniNumber(self, dniNumber: str) -> Optional[User]:
        session: Session = self.__databaseService.getSession()
        try:
            userModel: Optional[UserModel] = session.query(UserModel).filter_by(dni_number=dniNumber).first()
            return UserMapper.toDomain(userModel) if userModel is not None else None
        finally:
            session.close()
