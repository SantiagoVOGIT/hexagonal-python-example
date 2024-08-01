from enum import Enum


class InfrastructureErrorType(Enum):

    DATABASE_ERROR = "Error en la base de datos"
    USER_NOT_FOUND = "Este usuario no existe"
    CELL_NOT_FOUND = "Esta celda no existe"
    EMPLOYEE_NOT_FOUND = "Este empleado no existe"
    RESERVATION_NOT_FOUND = "Esta reserva no existe"
    VEHICLE_NOT_FOUND = "Este vehiculo no existe"
    ENV_DB_NOT_SET = "La URL de la base de datos no está configurada en las variables de entorno"
    ERROR_CONNECTION_DB = "Error al conectar con la base de datos"
