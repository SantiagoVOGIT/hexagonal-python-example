from typing import Optional

from src.shared.error.DomainException import DomainException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.DomainErrorType import DomainErrorType
from src.domain.entities.user.User import User
from src.domain.entities.user.UserFactory import UserFactory
from src.domain.entities.user.ports.UserRepository import UserRepository
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus
from src.domain.entities.user.ports.UserGateway import UserGateway


class UserUseCase(UserGateway):

    __userRepository: UserRepository

    def __init__(self, userOutputAdapter: UserRepository):
        self.__userRepository = userOutputAdapter

    def createUser(self,
                   dniNumber: Optional[str] = None,
                   dniType: Optional[DniType] = None,
                   firstName: Optional[str] = None,
                   lastName: Optional[str] = None,
                   emailAddress: Optional[str] = None,
                   phoneNumber: Optional[str] = None,
                   role: Optional[UserRole] = None,
                   status: Optional[UserStatus] = None
                   ) -> User:

        self.__validateNewDniNumber(dniNumber)
        self.__validateNewEmail(emailAddress)

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

    def register(self,
                 dniNumber: str,
                 dniType: DniType,
                 firstName: str,
                 lastName: str,
                 emailAddress: str,
                 phoneNumber: str,
                 ) -> User:

        return self.createUser(
            dniNumber=dniNumber,
            dniType=dniType,
            firstName=firstName,
            lastName=lastName,
            emailAddress=emailAddress,
            phoneNumber=phoneNumber,
            role=UserRole.USER,
            status=UserStatus.ACTIVE
        )

    def updateUser(self,
                   userId: UserId,
                   dniNumber: Optional[str] = None,
                   dniType: Optional[DniType] = None,
                   firstName: Optional[str] = None,
                   lastName: Optional[str] = None,
                   emailAddress: Optional[str] = None,
                   phoneNumber: Optional[str] = None,
                   role: Optional[UserRole] = None,
                   status: Optional[UserStatus] = None
                   ) -> None:

        self.__validateUserId(userId)

        user: Optional[User] = self.__userRepository.findById(userId)
        currentDniNumber: str = user.getDniNumber()
        currentEmailAddress: str = user.getEmailAddress()

        if currentDniNumber != dniNumber:
            self.__validateNewDniNumber(dniNumber)

        if currentEmailAddress != emailAddress:
            self.__validateNewEmail(emailAddress)

        updatedUser: User = UserFactory.update(
            user=user,
            dniNumber=dniNumber,
            dniType=dniType,
            firstName=firstName,
            lastName=lastName,
            emailAddress=emailAddress,
            phoneNumber=phoneNumber,
            role=role,
            status=status
        )
        self.__userRepository.updateUser(updatedUser)

    def __validateNewDniNumber(self, dniNumber: str) -> None:
        existingDniNumber: Optional[User] = self.__userRepository.findByDniNumber(dniNumber)
        if existingDniNumber is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.DNI_NUMBER_ALREADY_EXISTS
            ))

    def __validateNewEmail(self, emailAddress: str) -> None:
        existingEmail: Optional[User] = self.__userRepository.findByEmail(emailAddress)
        if existingEmail is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.EMAIL_ALREADY_EXISTS
            ))

    @staticmethod
    def __validateUserId(userId: UserId) -> None:
        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))
