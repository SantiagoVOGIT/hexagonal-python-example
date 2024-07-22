from datetime import datetime
from typing import Optional

from src.domain.models.user.value_objects.DniNumber import DniNumber
from src.domain.models.user.value_objects.DniType import DniType
from src.domain.models.user.value_objects.EmailAddress import EmailAddress
from src.domain.models.user.value_objects.PhoneNumber import PhoneNumber
from src.domain.models.user.value_objects.UserId import UserId
from src.domain.models.user.value_objects.UserRole import UserRole
from src.domain.models.user.value_objects.UserStatus import UserStatus


class User:

    __id: UserId
    __dniNumber: DniNumber
    __dniType: DniType
    __firstName: str
    __lastName: str
    __phoneNumber: PhoneNumber
    __emailAddress: EmailAddress
    __role: UserRole
    __status: UserStatus
    __createdAt: datetime
    __updatedAt: Optional[datetime]

    def __init__(self,
                 id: UserId,
                 dniNumber: DniNumber,
                 dniType: DniType,
                 firstName: str,
                 lastName: str,
                 role: UserRole,
                 status: UserStatus,
                 phoneNumber: Optional[PhoneNumber] = None,
                 emailAddress: Optional[EmailAddress] = None,
                 createdAt: Optional[datetime] = None,
                 updatedAt: Optional[datetime] = None
                 ):
        self.__id = id
        self.__dniNumber = dniNumber
        self.__dniType = dniType
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phoneNumber = phoneNumber
        self.__emailAddress = emailAddress
        self.__role = role
        self.__status = status
        self.__createdAt = User.__resolveCreatedAt(createdAt)
        self.__updatedAt = updatedAt

    def getId(self) -> UserId:
        return self.__id

    def getDniNumber(self) -> DniNumber:
        return self.__dniNumber

    def getDniType(self) -> DniType:
        return self.__dniType

    def getFirstName(self) -> str:
        return self.__firstName

    def getLastName(self) -> str:
        return self.__lastName

    def getPhoneNumber(self) -> Optional[PhoneNumber]:
        return self.__phoneNumber

    def getEmailAddress(self) -> Optional[EmailAddress]:
        return self.__emailAddress

    def getRole(self) -> UserRole:
        return self.__role

    def getStatus(self) -> UserStatus:
        return self.__status

    def getCreatedAt(self) -> datetime:
        return self.__createdAt

    def getUpdatedAt(self) -> Optional[datetime]:
        return self.__updatedAt

    @staticmethod
    def __resolveCreatedAt(createdAt: Optional[datetime] = None) -> datetime:
        return createdAt if createdAt else datetime.now()
