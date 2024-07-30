from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId


class ReservationDTO(BaseModel):

    reservationId: Optional[ReservationId] = Field(default=None)
    userId: Optional[UserId] = Field(default=None)
    cellId: Optional[CellId] = Field(default=None)
    vehicleId: Optional[VehicleId] = Field(default=None)
    status: Optional[ReservationStatus] = Field(default=None)
    endTime: Optional[datetime] = Field(default=None)

    @field_validator('reservationId', 'userId', 'cellId', 'vehicleId', mode='before')
    def validateId(cls, v, info):
        if v is None:
            return None
        id_class = globals()[info.field_name[0].upper() + info.field_name[1:]]
        if isinstance(v, id_class):
            return v
        try:
            return id_class(v)
        except ValueError as ex:
            raise ValueError(f'Invalid {info.field_name} format: {ex}')

    @field_validator('status', mode='before')
    def validateStatus(cls, v):
        if v is None:
            return None
        if isinstance(v, ReservationStatus):
            return v
        try:
            return ReservationStatus(v)
        except ValueError as ex:
            raise ValueError(f'Invalid ReservationStatus format: {ex}')

    class Config:
        use_enum_values = True
        arbitrary_types_allowed = True
        json_encoders = {
            ReservationId: lambda v: str(v.getValue()) if v else None,
            UserId: lambda v: str(v.getValue()) if v else None,
            CellId: lambda v: str(v.getValue()) if v else None,
            VehicleId: lambda v: str(v.getValue()) if v else None,
            ReservationStatus: lambda v: v.value if v else None,
        }

    def model_dump(self, *args, **kwargs):
        d = super().model_dump(*args, **kwargs)
        for field in ['reservationId', 'userId', 'cellId', 'vehicleId']:
            if d[field] is not None:
                d[field] = str(d[field].getValue())
        if d['status'] is not None:
            d['status'] = d['status'].value
        return d