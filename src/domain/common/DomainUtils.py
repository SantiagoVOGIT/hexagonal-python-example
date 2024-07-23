import re
from datetime import datetime, timezone
from typing import Optional, TypeVar, Type

from src.common.decorators.UtilityClass import utilityClass
from src.common.utils.ExceptionFactory import ExceptionFactory
from src.domain.common.enums.DomainError import DomainError

T = TypeVar('T')


@utilityClass
class DomainUtils:

    USER_NAME_PATTERN = re.compile(r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]{1,49}(-[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]{1,49})?$')
    DNI_PATTERN = re.compile(r"^\d{8,10}$")
    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9+_.-]+@(.+)$")
    PHONE_NUMBER_PATTERN = re.compile(r"^\d{10}$")
    LICENCE_PLATE_PATTERN = re.compile(r"^[A-Z]{3}\d{3}$")

    @staticmethod
    def isValidName(value: str) -> str:
        if not DomainUtils.USER_NAME_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_NAME_FORMAT)
                .getDetail()
            )
        return value

    @staticmethod
    def isValidDniNumber(value: str) -> str:
        if not DomainUtils.DNI_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_DNI_NUMBER_FORMAT).getDetail()
            )
        return value

    @staticmethod
    def isValidEmailAddress(value: str) -> str:
        if not DomainUtils.EMAIL_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_EMAIL_FORMAT)
                .getDetail()
            )
        return value

    @staticmethod
    def isValidPhoneNumber(value: str) -> str:
        if not DomainUtils.PHONE_NUMBER_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_PHONE_NUMBER_FORMAT)
                .getDetail()
            )
        return value

    @staticmethod
    def isValidLicensePlate(value: str) -> str:
        if not DomainUtils.LICENCE_PLATE_PATTERN.match(value):
            raise ValueError(
                ExceptionFactory
                .build(DomainError.INVALID_LICENSE_PLATE_FORMAT)
                .getDetail()
            )
        return value

    @staticmethod
    def resolveId(id: Optional[T], EntityId: Type[T]) -> T:
        return id if id is not None else EntityId.generate()

    @staticmethod
    def resolveCreatedAt(createdAt: Optional[datetime]) -> datetime:
        return createdAt if createdAt is not None else datetime.now(timezone.utc)

