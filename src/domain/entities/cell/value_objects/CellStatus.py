from enum import Enum


class CellStatus(Enum):

    AVAILABLE = "DISPONIBLE"
    OCCUPIED = "OCUPADA"
    MAINTENANCE = "MANTENIMIENTO"
    RESERVED = "RESERVADA"
    INACTIVE = "INACTIVA"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
