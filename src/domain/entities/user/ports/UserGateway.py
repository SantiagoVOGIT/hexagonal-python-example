from abc import ABC, abstractmethod
from typing import TypeVar, Optional

from src.domain.entities.user.User import User

T = TypeVar('T')


class UserGateway(ABC):

    @abstractmethod
    def createUser(self, user: User) -> User:
        pass

