from typing import Optional

from src.domain.entities.user.User import User
from src.domain.entities.user.UserFactory import UserFactory
from src.domain.entities.user.ports.UserGateway import UserGateway
from src.domain.entities.user.ports.UserRepository import UserRepository
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus


class UserUseCase(UserGateway):

    __userRepository: UserRepository

    def __init__(self, outputAdapter: UserRepository):
        self.__userRepository = outputAdapter

    def createUser(self, dniNumber: str, dniType: DniType, firstName: str, lastName: str, phoneNumber: str,
                   emailAddress: str, role: Optional[UserRole], status: Optional[UserStatus]) -> User:
        newUser: User = UserFactory.create(
            dniNumber=dniNumber,
            dniType=dniType,
            firstName=firstName,
            lastName=lastName,
            phoneNumber=phoneNumber,
            emailAddress=emailAddress,
            role=role,
            status=status
        )
        self.__userRepository.save(newUser)
        return newUser

    def updateUser(self, userId: str, firstName: str, lastName: str, phoneNumber: str, emailAddress: str) -> User:
        pass

    def changeUserStatus(self, userId: str, newStatus: str) -> User:
        pass
