from enum import Enum, unique


@unique
class UserRole(Enum):

    ADMIN = "ADMIN"
    USER = "USER"
    STAFF = "STAFF"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
