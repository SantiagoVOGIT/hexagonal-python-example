from enum import Enum


class ApplicationError(Enum):

    USER_ALREADY_EXISTS = "El usuario ya está registrado."
    USER_NOT_FOUND = "No se encontró un usuario asociado al correo ingresado."
    INVALID_PASSWORD = "La contraseña ingresada es incorrecta."
    INVALID_NAME_FORMAT = "Formato de nombre inválido"
    NOT_USERS_FOUND = "No se ha encontrado ninguna lista de usuarios"