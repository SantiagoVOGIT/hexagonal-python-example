from enum import Enum


class DniType(Enum):

    CC = "CÉDULA CIUDADANÍA"
    CE = "CÉDULA EXTRANJERÍA"
    TI = "TARJETA IDENTIDAD"
    TE = "TARJETA EXTRANJERÍA"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
