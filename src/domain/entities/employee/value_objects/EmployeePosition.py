from enum import Enum


class EmployeePosition(Enum):

    MANAGER = "GERENTE"
    CASHIER = "CAJERO"
    CAR_WASHER = "ASISTENTE DE LAVADO"
    MAINTENANCE = "MANTENIMIENTO"
    CUSTOMER_SERVICE = "SERVICIO AL CLIENTE"

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value
