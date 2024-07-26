from typing import Optional
from pydantic import BaseModel
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class CellDTO(BaseModel):

    spaceNumber: Optional[SpaceNumber] = None
    vehicleType: Optional[VehicleType] = None
    status: Optional[CellStatus] = None
