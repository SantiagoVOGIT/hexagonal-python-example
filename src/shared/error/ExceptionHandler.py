from enum import Enum
from typing import Dict, Any

from src.domain.common.EntityId import EntityId
from src.shared.error.CustomException import CustomException
from src.shared.error.enums.ErrorType import ErrorType


class ExceptionHandler:

    @staticmethod
    def raiseException(exception: CustomException) -> None:
        raise exception

    @staticmethod
    def handleException(exception: Exception) -> Dict[str, Any]:

        def make_serializable(obj):
            if isinstance(obj, EntityId):
                return str(obj)
            elif isinstance(obj, Enum):
                return obj.value
            elif isinstance(obj, dict):
                return {k: make_serializable(v) for k, v in obj.items()}
            elif isinstance(obj, (list, tuple)):
                return [make_serializable(item) for item in obj]
            return obj

        if isinstance(exception, CustomException):
            return {
                "error_type": make_serializable(exception.getErrorType()),
                "error_code": exception.getErrorCode(),
                "error_message": exception.getErrorMessage(),
                "additional_info": make_serializable(exception.getAdditionalInfo())
            }
        else:
            return {
                "error_type": ErrorType.APPLICATION_ERROR.value,
                "error_code": "UNEXPECTED_ERROR",
                "error_message": "Ha ocurrido un error inesperado",
                "additional_info": {"original_error": str(exception)}
            }
