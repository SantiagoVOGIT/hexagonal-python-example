from enum import Enum, unique


@unique
class VehicleType(Enum):

    CAR = "AUTOMÓVIL"
    MOTORCYCLE = "MOTOCICLETA"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value