from abc import ABC, abstractmethod
from typing import TypeVar, Optional

from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus

T = TypeVar('T')


class UserGateway(ABC):

    @abstractmethod
    def createUser(self,
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

    @abstractmethod
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
        pass
