from datetime import datetime
from typing import Optional
from src.shared.decorators.UtilityClass import utilityClass
from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus


@utilityClass
class UserFactory:

    @staticmethod
    def create(
            dniNumber: str,
            dniType: DniType,
            firstName: str,
            lastName: str,
            emailAddress: str,
            phoneNumber: str,
            role: UserRole = UserRole.USER,
            status: UserStatus = UserStatus.ACTIVE,
            id: Optional[UserId] = None,
            createdAt: Optional[datetime] = None
    ) -> User:
        return User(
            dniNumber=DomainUtils.validateDniNumber(dniNumber),
            firstName=DomainUtils.validateName(firstName),
            lastName=DomainUtils.validateName(lastName),
            emailAddress=DomainUtils.validateEmailAddress(emailAddress),
            phoneNumber=DomainUtils.validatePhoneNumber(phoneNumber),
            dniType=DomainUtils.validateEnum(dniType, DniType),
            role=DomainUtils.validateEnum(role, UserRole),
            status=DomainUtils.validateEnum(status, UserStatus),
            id=DomainUtils.resolveId(id, UserId),
            createdAt=DomainUtils.resolveCreatedAt(createdAt)
        )

    @staticmethod
    def update(
            user: User,
            dniNumber: Optional[str] = None,
            dniType: Optional[DniType] = None,
            firstName: Optional[str] = None,
            lastName: Optional[str] = None,
            emailAddress: Optional[str] = None,
            phoneNumber: Optional[str] = None,
            role: Optional[UserRole] = None,
            status: Optional[UserStatus] = None
    ) -> User:
        return User(
            id=user.getId(),
            dniNumber=DomainUtils.validateDniNumber(dniNumber) if dniNumber is not None else user.getDniNumber(),
            dniType=DomainUtils.validateEnum(dniType, DniType) if dniType is not None else user.getDniType(),
            firstName=DomainUtils.validateName(firstName) if firstName is not None else user.getFirstName(),
            lastName=DomainUtils.validateName(lastName) if lastName is not None else user.getLastName(),
            emailAddress=DomainUtils.validateEmailAddress(emailAddress) if emailAddress is not None else user.getEmailAddress(),
            phoneNumber=DomainUtils.validatePhoneNumber(phoneNumber) if phoneNumber is not None else user.getPhoneNumber(),
            role=DomainUtils.validateEnum(role, UserRole) if role is not None else user.getRole(),
            status=DomainUtils.validateEnum(status, UserStatus) if status is not None else user.getStatus(),
            createdAt=user.getCreatedAt()
        )
