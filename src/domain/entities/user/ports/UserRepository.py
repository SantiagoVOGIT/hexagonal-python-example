from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.user.User import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def findByEmail(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def findByDniNumber(self, dniNumber: str) -> Optional[User]:
        pass

