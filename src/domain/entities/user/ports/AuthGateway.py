from abc import ABC, abstractmethod
from typing import TypeVar

from src.domain.entities.user.User import User

T = TypeVar('T')


class AuthGateway(ABC):

    @abstractmethod
    def login(self, emailAddress: str, dniNumber: str) -> User:
        pass
