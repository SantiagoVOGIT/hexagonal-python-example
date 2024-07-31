from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.UserId import UserId


class UserRepository(ABC):

    @abstractmethod
    def saveUser(self, user: User) -> User:
        pass

    @abstractmethod
    def updateUser(self, user: User) -> None:
        pass

    @abstractmethod
    def findByEmail(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def findByDniNumber(self, dniNumber: str) -> Optional[User]:
        pass

    @abstractmethod
    def findById(self, userId: UserId) -> Optional[User]:
        pass
