import re
from datetime import datetime, timezone
from typing import Optional, TypeVar, Type, Union

from src.shared.decorators.UtilityClass import utilityClass
from src.shared.error.DomainException import DomainException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.DomainErrorType import DomainErrorType
from src.domain.entities.reservation.value_objects.ReservationCode import ReservationCode

T = TypeVar('T')


@utilityClass
class DomainUtils:

    USER_NAME_PATTERN = re.compile(r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]{1,50}$')
    DNI_PATTERN = re.compile(r"^\d{8,10}$")
    EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9+_.-]+@(.+)$")
    PHONE_NUMBER_PATTERN = re.compile(r"^\d{10}$")
    LICENCE_PLATE_PATTERN = re.compile(r"^[A-Z0-9]{1,7}$")
    SALARY_PATTERN = re.compile(r"^\d{1,8}(\.\d{1,2})?$")
    MODEL_PATTERN = re.compile(r'^[\w\s]{1,50}$')

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
        if not DomainUtils.EMAIL_PATTERN.match(value) or len(value) > 70:
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
    def validateSalary(value: float) -> float:
        if not DomainUtils.SALARY_PATTERN.match(str(value)):
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INVALID_SALARY_FORMAT
            ))
        return value

    @staticmethod
    def validateModel(value: str) -> str:
        if not DomainUtils.MODEL_PATTERN.match(value):
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INVALID_MODEL_FORMAT
            ))
        return value

    @staticmethod
    def validateEnum(value: Union[str, T], enumType: Type[T]) -> T:
        if isinstance(value, enumType):
            return value
        elif isinstance(value, str):
            try:
                return enumType(value)
            except ValueError:
                pass

        ExceptionHandler.raiseException(DomainException(
            DomainErrorType.INVALID_ENUM_VALUE,
            {"message": f"{value}, {enumType}"}
        ))

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
