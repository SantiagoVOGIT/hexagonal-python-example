from enum import Enum
from typing import Optional, Any


class CustomException(Exception):

    __errorCode: str
    __errorMessage: str
    __errorType: Enum

    def __init__(self, errorType: Enum):
        self.__errorCode = errorType.name
        self.__errorMessage = errorType.value
        self.__errorType = errorType

    def getCode(self) -> str:
        return self.__errorCode

    def getDetail(self, additionalData: Optional[Any] = None) -> str:
        if additionalData is not None:
            return f"{self.__errorMessage} detail: ... {additionalData}"
        return self.__errorMessage

    def getInfo(self):
        return f"Type: {self.__errorType}, Message: {self.__errorMessage}"

    def getType(self):
        return self.__errorType


class ExceptionFactory:

    @staticmethod
    def build(errorType: Enum) -> CustomException:
        return CustomException(errorType)

    @staticmethod
    def skipBuild(errorType: Enum, additionalData: Optional[Any] = None) -> str:
        return ExceptionFactory.build(errorType).getDetail(additionalData)
