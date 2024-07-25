from pydantic import BaseModel

from src.domain.entities.user.value_objects.DniType import DniType


class RegisterDTO(BaseModel):
    
    dniNumber: str
    dniType: DniType
    firstName: str
    lastName: str
    phoneNumber: str
    emailAddress: str
