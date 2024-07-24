from enum import Enum


class DomainErrorType(Enum):

    USER_ALREADY_EXISTS = "El usuario ya existe en el sistema"
    INCORRECT_LOGIN = "Credenciales de inicio de sesión incorrectas"
    INVALID_INPUT = "Datos de entrada inválidos"
    INVALID_DNI_NUMBER_FORMAT = "Formato de documento inválido"
    INVALID_EMAIL_FORMAT = "Formato de correo electrónico inválido"
    INVALID_PHONE_NUMBER_FORMAT = "Formato de número de teléfono inválido"
    INVALID_LICENSE_PLATE_FORMAT = "Formato de placa de vehiculo inválido"
    INVALID_NAME_FORMAT = "Formato de nombre o apellido inválido"