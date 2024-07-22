from enum import Enum, unique


@unique
class UserStatus(Enum):

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVO"
    SUSPENDED = "SUSPENDIDO"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value