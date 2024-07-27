from typing import Optional
from pydantic import BaseModel, validator
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.value_objects.UserId import UserId


class EmployeeDTO(BaseModel):

    userId: Optional[UserId] = None
    position: Optional[EmployeePosition] = None
    salary: Optional[float] = None

    @validator('userId', pre=True)
    def validate_user_id(cls, v):
        if v is None:
            return None
        if isinstance(v, UserId):
            return v
        try:
            return UserId(v)
        except ValueError as e:
            raise ValueError(f'Invalid UserId format: {e}')

    class Config:
        arbitrary_types_allowed = True

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        return {k: (v.getValue() if hasattr(v, 'getValue') else v) for k, v in d.items() if v is not None}
