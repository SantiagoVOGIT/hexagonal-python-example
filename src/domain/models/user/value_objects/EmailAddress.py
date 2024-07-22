from src.common.utils.ExceptionFactory import ExceptionFactory
from src.domain.common.DomainUtils import DomainUtils
from src.domain.common.enums.DomainError import DomainError


class EmailAddress:

    __value: str

    def __init__(self, value: str):
        self.__isValidEmailAddress(value)
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def __isValidEmailAddress(value: str) -> None:
        if not DomainUtils.EMAIL_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_EMAIL_FORMAT)
                .getDetail()
            )
