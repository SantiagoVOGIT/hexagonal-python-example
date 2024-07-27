from enum import Enum

from src.infrastructure.config.Environments import Environments


class InfrastructureInfo(Enum):

    SUCCESS_CONNECTION_DATABASE = "Conexión exitosa a la base de datos."
    CURRENT_ENVIRONMENT_API = f"Ambiente actual de la API: {Environments.getCurrentEnvironment()}."
    SUCCES_REGISTERED_USER = "Usuario registrado exitosamente."
    SUCCES_LOGIN = "Inicio de sesión exitoso"
    SUCCESS_CREATED_RESERVATION = "Reserva creada exitosamente"
    SUCCES_CREATED_CELL = "Celda creada exitosamente"
    SUCCES_CREATED_VEHICLE = "Vehículo credo exitosamente"
