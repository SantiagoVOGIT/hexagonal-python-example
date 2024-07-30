from abc import ABC, abstractmethod
from typing import TypeVar

from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType

T = TypeVar('T')


class AuthGateway(ABC):

    @abstractmethod
    def register(self,
                 dniNumber: str,
                 dniType: DniType,
                 firstName: str,
                 lastName: str,
                 phoneNumber: str,
                 emailAddress: str
                 ) -> User:
        pass

    @abstractmethod
    def login(self, emailAddress: str, dniNumber: str) -> User:
        pass
