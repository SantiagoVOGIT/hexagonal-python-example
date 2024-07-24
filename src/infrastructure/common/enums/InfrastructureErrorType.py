from enum import Enum


class InfrastructureErrorType(Enum):

    DATABASE_ERROR = "Error en la base de datos"
    USER_NOT_FOUND = "Usuario no encontrado"
    ENV_DB_NOT_SET = "La URL de la base de datos no está configurada en las variables de entorno"
    ERROR_CONNECTION_DB = "Error al conectar con la base de datos"
