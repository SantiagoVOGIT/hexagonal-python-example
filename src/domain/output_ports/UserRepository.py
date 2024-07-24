from abc import ABC, abstractmethod
from typing import TypeVar, Optional

from src.domain.entities.user.User import User

T = TypeVar('T')


class UserRepository(ABC):

    @abstractmethod
    def saveUser(self, user: User) -> None:
        pass

    @abstractmethod
    def findByEmail(self, emailAddress: str) -> Optional[User]:
        pass

    @abstractmethod
    def findByDniNumber(self, dniNumber: str) -> Optional[User]:
        pass