from typing import Optional

from pydantic import BaseModel

from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus


class UserDTO(BaseModel):

    dniNumber: Optional[str] = None
    dniType: Optional[DniType] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    phoneNumber: Optional[str] = None
    emailAddress: Optional[str] = None
    role: Optional[UserRole] = None
    status: Optional[UserStatus] = None
