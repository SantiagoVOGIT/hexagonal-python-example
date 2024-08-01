from enum import Enum


class UserRole(Enum):

    ADMIN = "ADMINISTRADOR"
    USER = "USUARIO"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
