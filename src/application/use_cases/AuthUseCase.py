from typing import Optional

from src.application.common.enums.ApplicationError import ApplicationError
from src.application.input_ports.AuthGateway import AuthGateway
from src.common.utils.ExceptionFactory import ExceptionFactory
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
        existingDniNumber: Optional[User] = self.__userRepository.findByDniNumber(dniNumber)

        if existingEmail is not None:
            raise ValueError(
                ExceptionFactory
                .build(ApplicationError.USER_ALREADY_EXISTS)
                .getDetail()
            )

        if existingDniNumber is not None:
            raise ValueError(
                ExceptionFactory
                .build(ApplicationError.USER_ALREADY_EXISTS)
                .getDetail()
            )

        newUser = UserFactory.create(
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
            raise ValueError(
                ExceptionFactory
                .build(ApplicationError.INCORRECT_LOGIN)
                .getDetail()
            )

        if user.getDniNumber() != dniNumber:
            raise ValueError(
                ExceptionFactory
                .build(ApplicationError.INCORRECT_LOGIN)
                .getDetail()
            )

        return user
