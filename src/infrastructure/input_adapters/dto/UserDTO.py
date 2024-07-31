
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus

class UserDTO(BaseModel):

    dniNumber: Optional[str] = Field(default=None)
    dniType: Optional[DniType] = Field(default=None)
    firstName: Optional[str] = Field(default=None)
    lastName: Optional[str] = Field(default=None)
    phoneNumber: Optional[str] = Field(default=None)
    emailAddress: Optional[str] = Field(default=None)
    role: Optional[UserRole] = Field(default=None)
    status: Optional[UserStatus] = Field(default=None)

    @field_validator('dniType', 'role', 'status', mode='before')
    def validateEnum(cls, v, info):
        if v is None:
            return None
        enum_map = {
            'dniType': DniType,
            'role': UserRole,
            'status': UserStatus
        }
        enum_class = enum_map.get(info.field_name)
        if enum_class is None:
            raise ValueError(f'Unknown enum field: {info.field_name}')
        if isinstance(v, enum_class):
            return v
        try:
            return enum_class(v)
        except ValueError as ex:
            raise ValueError(f'Invalid {info.field_name} format: {ex}')

    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True
        json_encoders = {
            DniType: lambda v: v.value if v else None,
            UserRole: lambda v: v.value if v else None,
            UserStatus: lambda v: v.value if v else None,
        }

    def model_dump(self, *args, **kwargs):
        d = super().model_dump(*args, **kwargs)
        for field in ['dniType', 'role', 'status']:
            if d[field] is not None:
                d[field] = d[field].value
        return d