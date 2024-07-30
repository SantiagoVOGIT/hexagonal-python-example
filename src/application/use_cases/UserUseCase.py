from src.domain.entities.user.User import User
from src.domain.entities.user.UserFactory import UserFactory
from src.domain.entities.user.ports.UserRepository import UserRepository
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus
from src.domain.entities.user.ports.UserGateway import UserGateway


class UserUseCase(UserGateway):

    __userRepository: UserRepository

    def __init__(self, userOutputAdapter: UserRepository):
        self.__userRepository = userOutputAdapter

    def createFullUser(self,
                       dniNumber: str,
                       dniType: DniType,
                       firstName: str,
                       lastName: str,
                       emailAddress: str,
                       phoneNumber: str,
                       role: UserRole,
                       status: UserStatus
                       ) -> User:

        newUser: User = UserFactory.create(
            dniNumber=dniNumber,
            dniType=dniType,
            firstName=firstName,
            lastName=lastName,
            emailAddress=emailAddress,
            phoneNumber=phoneNumber,
            role=role,
            status=status
        )
        self.__userRepository.saveUser(newUser)
        return newUser
