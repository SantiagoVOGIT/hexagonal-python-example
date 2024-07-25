import re
from datetime import datetime, timezone
from typing import Optional, TypeVar, Type

from src.shared.decorators.UtilityClass import utilityClass
from src.shared.utils.ErrorHandler import DomainException, ExceptionHandler
from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.reservation.value_objects.ReservationCode import ReservationCode

T = TypeVar('T')


@utilityClass
class DomainUtils:

    USER_NAME_PATTERN = re.compile(r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]{1,49}(-[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]{1,49})?$')
    DNI_PATTERN = re.compile(r"^\d{8,10}$")
    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9+_.-]+@(.+)$")
    PHONE_NUMBER_PATTERN = re.compile(r"^\d{10}$")
    LICENCE_PLATE_PATTERN = re.compile(r"^[A-Z]{3}\d{3}$")

    @staticmethod
    def validateName(value: str) -> str:
        if not DomainUtils.USER_NAME_PATTERN.match(value):
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INVALID_NAME_FORMAT
            ))
        return value

    @staticmethod
    def validateDniNumber(value: str) -> str:
        if not DomainUtils.DNI_PATTERN.match(value):
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INVALID_DNI_NUMBER_FORMAT
            ))
        return value

    @staticmethod
    def validateEmailAddress(value: str) -> str:
        if not DomainUtils.EMAIL_PATTERN.match(value):
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INVALID_EMAIL_FORMAT
            ))
        return value

    @staticmethod
    def validatePhoneNumber(value: str) -> str:
        if not DomainUtils.PHONE_NUMBER_PATTERN.match(value):
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INVALID_PHONE_NUMBER_FORMAT
            ))
        return value

    @staticmethod
    def validateLicensePlate(value: str) -> str:
        if not DomainUtils.LICENCE_PLATE_PATTERN.match(value):
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INVALID_LICENSE_PLATE_FORMAT
            ))
        return value

    @staticmethod
    def resolveId(id: Optional[T], EntityId: Type[T]) -> T:
        return (id
                if id is not None
                else EntityId.generate())

    @staticmethod
    def resolveCreatedAt(createdAt: Optional[datetime]) -> datetime:
        return (createdAt
                if createdAt is not None
                else datetime.now(timezone.utc))

    @staticmethod
    def resolveReservationCode(reservationCode: Optional[ReservationCode]) -> ReservationCode:
        return (reservationCode
                if reservationCode is not None
                else ReservationCode.generate())
