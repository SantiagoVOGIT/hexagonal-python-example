from src.common.utils.ExceptionFactory import ExceptionFactory
from src.domain.common.DomainUtils import DomainUtils
from src.domain.common.enums.DomainError import DomainError


class LicensePlate:

    __value: str

    def __init__(self, value: str):
        self.__isValidLicensePlate(value)
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def __isValidLicensePlate(value: str) -> None:
        if not DomainUtils.LICENCE_PLATE_FORMAT.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_LICENSE_PLATE)
                .getDetail()
            )
