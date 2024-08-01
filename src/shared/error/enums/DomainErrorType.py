from enum import Enum


class DomainErrorType(Enum):

    RESERVATIONS_NOT_FOUND = "No se encontró ninguna reserva"
    SPACE_NUMBER_ALREADY_EXISTS = "Este número de celda ya se encuentra asociado a otra celda"
    EMAIL_ALREADY_EXISTS = "Este correo electrónico ya se encuentra asociado a otro usuario"
    DNI_NUMBER_ALREADY_EXISTS = "Este número de identificación ya se encuentra asociado a otro usuario"
    USER_NOT_FOUND = "Este usuario no existe"
    INVALID_INPUT = "Datos de entrada inválidos."
    INVALID_ENUM_VALUE = "Propiedad inválida."
    INVALID_DNI_NUMBER_FORMAT = "Formato de documento inválido."
    INVALID_EMAIL_FORMAT = "Formato de correo electrónico inválido."
    INVALID_PHONE_NUMBER_FORMAT = "Formato de número de teléfono inválido."
    INVALID_LICENSE_PLATE_FORMAT = "Formato de placa de vehículo inválido."
    INVALID_NAME_FORMAT = "Formato de nombre o apellido inválido."
    INVALID_SALARY_FORMAT = "Formato de salario inválido."
    INVALID_MODEL_FORMAT = "Formato de modelo de vehículo inválido."
    INCORRECT_LOGIN = "Credenciales de inicio de sesión incorrectas."
    USER_ID_REQUIRED = "No se puede realizar esta acción sin un usuario asociado."
    USER_ALREADY_EXISTS = "Este usuario ya existe en el sistema."
    EMPLOYEE_ALREADY_EXISTS = "Este empleado ya se encuentra asociado a otro usuario"
    VEHICLE_ALREADY_EXISTS = "Esta placa ya se encuentra asociada a otro vehículo"
    CELL_ALREADY_EXISTS = "Este número de celda ya está asociado con otra celda."
    CELL_NOT_AVAILABLE = "No es posible reservar esta celda en estos momentos"
    INCOMPATIBLE_VEHICLE_TYPE_CELL = "Su tipo de vehiculo no es compatible con esta celda"
