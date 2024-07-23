from enum import Enum, unique


@unique
class UserRole(Enum):

    ADMIN = "ADMINISTRADOR"
    USER = "USUARIO"
    STAFF = "EMPLEADO"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
