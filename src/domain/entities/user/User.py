from datetime import datetime
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus


class User:

    __id: UserId
    __dniNumber: str
    __dniType: DniType
    __firstName: str
    __lastName: str
    __phoneNumber: str
    __emailAddress: str
    __role: UserRole
    __status: UserStatus
    __createdAt: datetime

    def __init__(self,
                 dniNumber: str,
                 dniType: DniType,
                 firstName: str,
                 lastName: str,
                 role: UserRole,
                 emailAddress: str,
                 status: UserStatus = UserStatus.ACTIVE,
                 phoneNumber: Optional[str] = None,
                 id: Optional[UserId] = None,
                 createdAt: Optional[datetime] = None
                 ):
        self.__id = DomainUtils.resolveId(id, UserId)
        self.__dniNumber = DomainUtils.isValidDniNumber(dniNumber)
        self.__dniType = dniType
        self.__firstName = DomainUtils.isValidName(firstName)
        self.__lastName = DomainUtils.isValidName(lastName)
        self.__phoneNumber = DomainUtils.isValidPhoneNumber(phoneNumber)
        self.__emailAddress = DomainUtils.isValidEmailAddress(emailAddress)
        self.__role = role
        self.__status = status
        self.__createdAt = DomainUtils.resolveCreatedAt(createdAt)

    def getId(self) -> UserId:
        return self.__id

    def getDniNumber(self) -> str:
        return self.__dniNumber

    def getDniType(self) -> DniType:
        return self.__dniType

    def getFirstName(self) -> str:
        return self.__firstName

    def getLastName(self) -> str:
        return self.__lastName

    def getPhoneNumber(self) -> Optional[str]:
        return self.__phoneNumber

    def getEmailAddress(self) -> Optional[str]:
        return self.__emailAddress

    def getRole(self) -> UserRole:
        return self.__role

    def getStatus(self) -> UserStatus:
        return self.__status

    def getCreatedAt(self) -> datetime:
        return self.__createdAt



