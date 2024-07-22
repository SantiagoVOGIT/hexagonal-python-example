from enum import Enum
from typing import Optional, Any


class Message:

    __code: str
    __message: str
    __messageType: Enum

    def __init__(self, messageType: Enum):
        self.__code = messageType.name
        self.__message = messageType.value
        self.__messageType = messageType

    def getCode(self) -> str:
        return self.__code

    def getDetail(self, additionalData: Optional[Any] = None) -> str:
        if additionalData is not None:
            return f"{self.__message} detail: ... {additionalData}"
        return self.__message

    def getType(self) -> Enum:
        return self.__messageType


class MessageFactory:

    @staticmethod
    def build(messageType: Enum) -> Message:
        return Message(messageType)

    @staticmethod
    def skipBuild(messageType: Enum, additionalData: Optional[Any] = None) -> str:
        return MessageFactory.build(messageType).getDetail(additionalData)
