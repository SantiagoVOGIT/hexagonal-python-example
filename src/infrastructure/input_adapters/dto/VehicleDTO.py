# src/infrastructure/input_adapters/dto/VehicleDTO.py
from typing import Optional
from pydantic import BaseModel, validator
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class VehicleDTO(BaseModel):

    userId: Optional[UserId] = None
    licensePlate: Optional[str] = None
    model: Optional[str] = None
    vehicleType: Optional[VehicleType] = None

    @validator('userId', pre=True)
    def validate_user_id(cls, v):
        if v is None:
            return None
        if isinstance(v, UserId):
            return v
        try:
            return UserId(v)
        except ValueError as ex:
            raise ValueError(f'Invalid Id format: {ex}')

    class Config:
        arbitrary_types_allowed = True
