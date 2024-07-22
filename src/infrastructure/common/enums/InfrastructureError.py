from enum import Enum


class InfrastructureError(Enum):

    ERROR_CONNECTION_DB = "Ha ocurrido un error al intentar conectarse a la base de datos."
    ENV_DB_NOT_SET = "No se ha configurado la URL de la base de datos en las variables de entorno"
