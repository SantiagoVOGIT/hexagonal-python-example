from typing import Optional

from pydantic import BaseModel

from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class VehicleDTO(BaseModel):

    userId: Optional[UserId] = None
    licensePlate: Optional[str] = None
    model: Optional[str] = None
    vehicleType: Optional[VehicleType] = None
