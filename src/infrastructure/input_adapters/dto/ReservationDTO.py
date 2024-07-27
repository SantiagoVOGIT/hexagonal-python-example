from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId


class ReservationDTO(BaseModel):
    userId: Optional[UserId] = None
    cellId: Optional[CellId] = None
    vehicleId: Optional[VehicleId] = None
    status: Optional[ReservationStatus] = None
    endTime: Optional[datetime] = None

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

    @validator('cellId', pre=True)
    def validate_cell_id(cls, v):
        if v is None:
            return None
        if isinstance(v, CellId):
            return v
        try:
            return CellId(v)
        except ValueError as e:
            raise ValueError(f'Invalid CellId format: {e}')

    @validator('vehicleId', pre=True)
    def validate_vehicle_id(cls, v):
        if v is None:
            return None
        if isinstance(v, VehicleId):
            return v
        try:
            return VehicleId(v)
        except ValueError as e:
            raise ValueError(f'Invalid VehicleId format: {e}')

    class Config:
        arbitrary_types_allowed = True

    def dict(self, *args, **kwargs):
        d = super().dict(*args, **kwargs)
        return {k: (v.getValue() if hasattr(v, 'getValue') else v) for k, v in d.items() if v is not None}
