from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional

from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus

T = TypeVar('T')


class UserGateway(ABC):

    @abstractmethod
    def createUser(self, dniNumber: str, dniType: DniType, firstName: str, lastName: str, phoneNumber: str,
                   emailAddress: str, role: Optional[UserRole], status: Optional[UserStatus]) -> User:
        pass

    @abstractmethod
    def updateUser(self, userId: str, firstName: str, lastName: str, phoneNumber: str, emailAddress: str) -> User:
        pass

    @abstractmethod
    def changeUserStatus(self, userId: str, newStatus: str) -> User:
        pass
