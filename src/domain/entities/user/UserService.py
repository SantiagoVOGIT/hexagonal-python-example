from typing import Optional

from src.domain.entities.user.User import User
from src.domain.entities.user.UserFactory import UserFactory
from src.domain.entities.user.ports.UserGateway import UserGateway
from src.domain.entities.user.ports.UserRepository import UserRepository
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole


class UserService(UserGateway):
    def __init__(self, outputAdapter: UserRepository):
        self.__userRepository = outputAdapter

    def createUser(self, user: User) -> User:
        self.__userRepository.save(user)
        return user
