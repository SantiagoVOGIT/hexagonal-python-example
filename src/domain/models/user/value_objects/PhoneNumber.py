from src.common.utils.ExceptionFactory import ExceptionFactory
from src.domain.common.DomainUtils import DomainUtils
from src.domain.common.enums.DomainError import DomainError


class PhoneNumber:

    __value: str

    def __init__(self, value: str):
        self.__isValidPhoneNumber(value)
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def __isValidPhoneNumber(value: str) -> None:
        if not DomainUtils.PHONE_NUMBER_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_PHONE_NUMBER_FORMAT)
                .getDetail()
            )
