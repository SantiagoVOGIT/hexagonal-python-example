from enum import Enum, unique


@unique
class CellStatus(Enum):

    AVAILABLE = "DISPONIBLE"
    OCCUPIED = "OCUPADA"
    MAINTENANCE = "MANTENIMIENTO"
    RESERVED = "RESERVADA"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
