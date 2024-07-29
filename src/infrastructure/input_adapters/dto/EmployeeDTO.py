from typing import Optional
from pydantic import BaseModel, Field, field_validator
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.value_objects.UserId import UserId


class EmployeeDTO(BaseModel):

    userId: Optional[UserId] = Field(default=None)
    position: Optional[EmployeePosition] = Field(default=None)
    salary: Optional[float] = Field(default=None)

    @field_validator('userId', mode='before')
    def validateUserId(cls, v):
        if v is None:
            return None
        if isinstance(v, UserId):
            return v
        try:
            return UserId(v)
        except ValueError as ex:
            raise ValueError(f'Invalid UserId format: {ex}')

    @field_validator('position', mode='before')
    def validatePosition(cls, v):
        if v is None:
            return None
        if isinstance(v, EmployeePosition):
            return v
        try:
            return EmployeePosition(v)
        except ValueError as ex:
            raise ValueError(f'Invalid EmployeePosition format: {ex}')

    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True
        json_encoders = {
            UserId: lambda v: str(v.getValue()) if v else None,
            EmployeePosition: lambda v: v.value if v else None,
        }

    def model_dump(self, *args, **kwargs):
        d = super().model_dump(*args, **kwargs)
        if d['userId'] is not None:
            d['userId'] = str(d['userId'].getValue())
        if d['position'] is not None:
            d['position'] = d['position'].value
        return d
