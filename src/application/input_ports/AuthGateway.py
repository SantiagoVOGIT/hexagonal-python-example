from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType


class AuthInputPort(ABC):

    @abstractmethod
    def register(self,
                 dniNumber: str,
                 dniType: DniType,
                 firstName: str,
                 lastName: str,
                 phoneNumber: Optional[str],
                 emailAddress: str) -> User:
        pass

    @abstractmethod
    def login(self, emailAddress: str, dniNumber: str) -> User:
        pass
