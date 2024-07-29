from typing import Optional
from pydantic import BaseModel, Field, field_validator
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class VehicleDTO(BaseModel):

    userId: Optional[UserId] = Field(default=None)
    licensePlate: Optional[str] = Field(default=None)
    model: Optional[str] = Field(default=None)
    vehicleType: Optional[VehicleType] = Field(default=None)

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

    @field_validator('vehicleType', mode='before')
    def validateVehicleType(cls, v):
        if v is None:
            return None
        if isinstance(v, VehicleType):
            return v
        try:
            return VehicleType(v)
        except ValueError as ex:
            raise ValueError(f'Invalid VehicleType format: {ex}')

    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True
        json_encoders = {
            UserId: lambda v: str(v.getValue()) if v else None,
            VehicleType: lambda v: v.value if v else None,
        }

    def model_dump(self, *args, **kwargs):
        d = super().model_dump(*args, **kwargs)
        if d['userId'] is not None:
            d['userId'] = str(d['userId'].getValue())
        if d['vehicleType'] is not None:
            d['vehicleType'] = d['vehicleType'].value
        return d
