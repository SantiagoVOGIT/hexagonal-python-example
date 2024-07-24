from typing import Optional

from src.application.input_ports.AuthGateway import AuthGateway
from src.common.utils.ErrorHandler import ExceptionHandler, DomainException
from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.user.User import User
from src.domain.entities.user.UserFactory import UserFactory
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.output_ports.UserRepository import UserRepository


class AuthUseCase(AuthGateway):

    __userRepository: UserRepository

    def __init__(self, outputPort: UserRepository):
        self.__userRepository = outputPort

    def register(self, dniNumber: str, dniType: DniType, firstName: str, lastName: str, phoneNumber: str,
                 emailAddress: str) -> User:

        existingEmail: Optional[User] = self.__userRepository.findByEmail(emailAddress)
        if existingEmail is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ALREADY_EXISTS,
                {"email": emailAddress}
            ))

        existingDniNumber: Optional[User] = self.__userRepository.findByDniNumber(dniNumber)
        if existingDniNumber is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ALREADY_EXISTS,
                {"dni_number": dniNumber}
            ))

        newUser: User = UserFactory.create(
            dniNumber=dniNumber,
            dniType=dniType,
            firstName=firstName,
            lastName=lastName,
            phoneNumber=phoneNumber,
            emailAddress=emailAddress
        )

        self.__userRepository.saveUser(newUser)
        return newUser

    def login(self, emailAddress: str, dniNumber: str) -> User:
        user: Optional[User] = self.__userRepository.findByEmail(emailAddress)

        if user is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INCORRECT_LOGIN,
                {"email": emailAddress}
            ))

        if user.getDniNumber() != dniNumber:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INCORRECT_LOGIN,
                {"email": emailAddress}
            ))

        return user
