from datetime import datetime
from typing import Optional
from pydantic import BaseModel
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
