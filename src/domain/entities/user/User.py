from datetime import datetime
from typing import Dict, Any

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
                 id: UserId,
                 dniNumber: str,
                 dniType: DniType,
                 firstName: str,
                 lastName: str,
                 emailAddress: str,
                 role: UserRole,
                 status: UserStatus,
                 phoneNumber: str,
                 createdAt: datetime):
        self.__id = id
        self.__dniNumber = dniNumber
        self.__dniType = dniType
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phoneNumber = phoneNumber
        self.__emailAddress = emailAddress
        self.__role = role
        self.__status = status
        self.__createdAt = createdAt

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

    def getPhoneNumber(self) -> str:
        return self.__phoneNumber

    def getEmailAddress(self) -> str:
        return self.__emailAddress

    def getRole(self) -> UserRole:
        return self.__role

    def getStatus(self) -> UserStatus:
        return self.__status

    def getCreatedAt(self) -> datetime:
        return self.__createdAt

    @staticmethod
    def toDict(user: 'User') -> Dict[str, Any]:
        return {
            "id": user.getId().getValue(),
            "dniNumber": user.getDniNumber(),
            "dniType": user.getDniType().value,
            "firstName": user.getFirstName(),
            "lastName": user.getLastName(),
            "phoneNumber": user.getPhoneNumber(),
            "emailAddress": user.getEmailAddress(),
            "role": user.getRole().value,
            "status": user.getStatus().value,
            "createdAt": user.getCreatedAt().isoformat()
        }
