from typing import Optional

from pydantic import BaseModel

from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.value_objects.UserId import UserId


class EmployeeDTO(BaseModel):

    userId: Optional[UserId] = None
    position: Optional[EmployeePosition] = None
    salary: Optional[float] = None
