from enum import Enum


class ReservationStatus(Enum):

    PENDING = "PENDIENTE"
    CONFIRMED = "CONFIRMADA"
    CANCELLED = "CANCELADA"
    COMPLETED = "COMPLETADA"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

