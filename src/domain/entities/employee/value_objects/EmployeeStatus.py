from enum import Enum


class EmployeeStatus(Enum):

    ACTIVE = "ACTIVO"
    INACTIVE = "INACTIVO"
    VACATION = "VACACIONES"
    LEAVE = "LICENCIA"
    SUSPENDED = "SUSPENDIDO"
    RETIRED = "RETIRADO"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
