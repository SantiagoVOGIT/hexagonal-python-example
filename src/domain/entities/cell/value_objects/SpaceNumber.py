from enum import Enum, unique


@unique
class SpaceNumber(Enum):

    CELDA_UNO = "1"
    CELDA_DOS = "2"
    CELDA_TRES = "3"
    CELDA_CUATRO = "4"
    CELDA_CINCO = "5"
    CELDA_SEIS = "6"
    CELDA_SIETE = "7"
    CELDA_OCHO = "8"
    CELDA_NUEVE = "9"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
