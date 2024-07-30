from typing import Optional
from pydantic import BaseModel, Field, field_validator

from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class CellDTO(BaseModel):

    cellId: Optional[CellId] = Field(default=None)
    spaceNumber: Optional[SpaceNumber] = Field(default=None)
    vehicleType: Optional[VehicleType] = Field(default=None)
    status: Optional[CellStatus] = Field(default=None)

    @field_validator('cellId', mode='before')
    def validateId(cls, v):
        if v is None:
            return None
        if isinstance(v, CellId):
            return v
        try:
            return CellId(v)
        except ValueError as ex:
            raise ValueError(f'Invalid CellId format: {ex}')

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

    @field_validator('status', mode='before')
    def validateStatus(cls, v):
        if v is None:
            return None
        if isinstance(v, CellStatus):
            return v
        try:
            return CellStatus(v)
        except ValueError as ex:
            raise ValueError(f'Invalid CellStatus format: {ex}')

    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True
        json_encoders = {
            SpaceNumber: lambda v: str(v.getValue()) if v else None,
            VehicleType: lambda v: v.value if v else None,
            CellStatus: lambda v: v.value if v else None,
        }

    def model_dump(self, *args, **kwargs):
        d = super().model_dump(*args, **kwargs)
        if d['spaceNumber'] is not None:
            d['spaceNumber'] = str(d['spaceNumber'].getValue())
        if d['vehicleType'] is not None:
            d['vehicleType'] = d['vehicleType'].value
        if d['status'] is not None:
            d['status'] = d['status'].value
        return d
