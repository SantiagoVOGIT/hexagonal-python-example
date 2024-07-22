from src.common.utils.ExceptionFactory import ExceptionFactory
from src.domain.common.DomainUtils import DomainUtils
from src.domain.common.enums.DomainError import DomainError


class DniNumber:

    __value: str

    def __init__(self, value: str):
        self.__isValidDniNumber(value)
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def __isValidDniNumber(value: str) -> None:
        if not DomainUtils.DNI_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_DNI_NUMBER_FORMAT).getDetail()
            )
