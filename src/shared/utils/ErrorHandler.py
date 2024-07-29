from enum import Enum
from typing import Dict, Any, Optional

from src.domain.common.EntityId import EntityId
from src.domain.common.enums.DomainErrorType import DomainErrorType


class ErrorType(Enum):

    DOMAIN_ERROR = "Error de dominio"
    INFRASTRUCTURE_ERROR = "Error de infraestructura"
    APPLICATION_ERROR = "Error de aplicación"


class CustomException(Exception):

    __errorType: ErrorType
    __errorCode: str
    __errorMessage: str
    __additionalInfo: Dict[str, Any]

    def __init__(self, errorType: ErrorType, errorCode: str, errorMessage: str,
                 additionalInfo: Optional[Dict[str, Any]] = None):
        self.__errorType = errorType
        self.__errorCode = errorCode
        self.__errorMessage = errorMessage
        self.__additionalInfo = additionalInfo or {}

    def getErrorType(self) -> ErrorType:
        return self.__errorType

    def getErrorCode(self) -> str:
        return self.__errorCode

    def getErrorMessage(self) -> str:
        return self.__errorMessage

    def getAdditionalInfo(self) -> Dict[str, Any]:
        return self.__additionalInfo


class DomainException(CustomException):
    def __init__(self, domainErrorType: DomainErrorType, additionalInfo: Optional[Dict[str, Any]] = None):
        super().__init__(
            ErrorType.DOMAIN_ERROR,
            domainErrorType.name,
            domainErrorType.value,
            additionalInfo
        )


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