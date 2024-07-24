from enum import Enum


class ApplicationError(Enum):

    USER_ALREADY_EXISTS = "El usuario ya se encuentra registrado."
    INCORRECT_LOGIN = "El número de identificación o correo eléctronico son incorrectos."
