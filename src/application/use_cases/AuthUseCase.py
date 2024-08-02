from typing import Optional

from src.domain.entities.user.User import User
from src.domain.entities.user.ports.AuthGateway import AuthGateway
from src.domain.entities.user.ports.UserRepository import UserRepository
from src.shared.error.DomainException import DomainException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.DomainErrorType import DomainErrorType


class AuthUseCase(AuthGateway):

    __userRepository: UserRepository

    def __init__(self, userOutputAdapter: UserRepository):
        self.__userRepository = userOutputAdapter

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
                {"dniNumber": dniNumber}
            ))
        return user
