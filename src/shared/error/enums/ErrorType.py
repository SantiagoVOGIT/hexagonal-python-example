from enum import Enum


class ErrorType(Enum):

    DOMAIN_ERROR = "Error de dominio"
    INFRASTRUCTURE_ERROR = "Error de infraestructura"
    APPLICATION_ERROR = "Error de aplicación"
