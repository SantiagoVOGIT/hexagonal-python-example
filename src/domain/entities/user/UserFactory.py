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
               role: UserRole = UserRole.USER,
               status: UserStatus = UserStatus.ACTIVE,
               phoneNumber: Optional[str] = None,
               id: Optional[UserId] = None,
               createdAt: Optional[datetime] = None) -> User:

        ensureId = DomainUtils.resolveId(id, UserId)
        validatedDniNumber = DomainUtils.isValidDniNumber(dniNumber)
        validatedFirstName = DomainUtils.isValidName(firstName)
        validatedLastName = DomainUtils.isValidName(lastName)
        validatedPhoneNumber = DomainUtils.isValidPhoneNumber(phoneNumber) if phoneNumber else None
        validatedEmailAddress = DomainUtils.isValidEmailAddress(emailAddress)
        ensureCreatedAt = DomainUtils.resolveCreatedAt(createdAt)

        return User(
            id=ensureId,
            dniNumber=validatedDniNumber,
            dniType=dniType,
            firstName=validatedFirstName,
            lastName=validatedLastName,
            emailAddress=validatedEmailAddress,
            role=role,
            status=status,
            phoneNumber=validatedPhoneNumber,
            createdAt=ensureCreatedAt
        )
