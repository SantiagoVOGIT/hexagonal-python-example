from abc import ABC, abstractmethod
from typing import TypeVar

from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus

T = TypeVar('T')


class UserGateway(ABC):

    @abstractmethod
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
        pass
