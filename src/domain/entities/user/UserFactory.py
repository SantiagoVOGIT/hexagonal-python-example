from datetime import datetime
from typing import Optional

from src.common.decorators.UtilityClass import utilityClass
from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus


@utilityClass
class UserFactory:

    @staticmethod
    def create(dniNumber: str,
               dniType: DniType,
               firstName: str,
               lastName: str,
               emailAddress: str,
               phoneNumber: str,
               role: UserRole = UserRole.USER,
               status: UserStatus = UserStatus.ACTIVE,
               id: Optional[UserId] = None,
               createdAt: Optional[datetime] = None) -> User:

        return User(
            id=DomainUtils.resolveId(id, UserId),
            dniNumber=DomainUtils.validateDniNumber(dniNumber),
            dniType=dniType,
            firstName=DomainUtils.validateName(firstName),
            lastName=DomainUtils.validateName(lastName),
            emailAddress=DomainUtils.validateEmailAddress(emailAddress),
            role=role,
            status=status,
            phoneNumber=DomainUtils.validatePhoneNumber(phoneNumber),
            createdAt=DomainUtils.resolveCreatedAt(createdAt)
        )
