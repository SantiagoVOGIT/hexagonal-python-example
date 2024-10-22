from enum import Enum

from src.infrastructure.config.Environments import Environments


class InfrastructureInfo(Enum):

    SUCCESS_UPDATE_VEHICLE = "Vehículo actualizado exitosamente"
    SUCCESS_CREATED_CELL = "Celda creada exitosamente"
    SUCCES_UPDATED_USER_BASIC_INFO = "Información personal actualizada exitosamente"
    SUCCESS_UPDATED_VEHICLE = "Vehiculo actualizado exitosamente"
    SUCCESS_CREATED_USER = "Usuario creado exitosamente"
    SUCCESS_UPDATED_USER = "Usuario actualizado exitosamente"
    SUCCESS_UPDATED_CELL = "Celda actualizada exitosamente"
    SUCCESS_UPDATED_EMPLOYEE = "Empleado actualizado exitosamente"
    SUCCESS_COMPLETE_RESERVATION = "Reserva completa exitosamente"
    SUCCESS_CONFIRM_RESERVATION = "Reserva confirmada exitosamente"
    SUCCESS_CANCEL_RESERVATION = "Reserva cancelada exitosamente"
    SUCCESS_REJECT_RESERVATION = "Reserva rechazada exitosamente"
    SUCCES_UPDATED_CELL = "Celda modificada exitosamente"
    SUCCESS_CONNECTION_DATABASE = "Conexión exitosa a la base de datos."
    SUCCES_REGISTERED_USER = "Cuenta creada exitosamente."
    SUCCES_LOGIN = "Inicio de sesión exitoso"
    SUCCESS_CREATED_RESERVATION = "Reserva creada exitosamente"
    SUCCES_CREATED_CELL = "Celda creada exitosamente"
    SUCCES_CREATED_VEHICLE = "Vehículo creado exitosamente"
    SUCCES_CREATED_EMPLOYEE = "Empleado creado correctamente"
    CURRENT_ENVIRONMENT_API = f"Ambiente actual de la API: {Environments.getCurrentEnvironment()}."
