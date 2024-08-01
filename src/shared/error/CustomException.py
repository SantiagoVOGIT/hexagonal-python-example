from typing import Dict, Any, Optional

from src.shared.error.enums.ErrorType import ErrorType


class CustomException(Exception):

    __errorType: ErrorType
    __errorCode: str
    __errorMessage: str
    __additionalInfo: Dict[str, Any]

    def __init__(self,
                 errorType: ErrorType,
                 errorCode: str,
                 errorMessage: str,
                 additionalInfo: Optional[Dict[str, Any]] = None
                 ):
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
