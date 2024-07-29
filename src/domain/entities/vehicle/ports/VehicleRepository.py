from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class VehicleRepository(ABC):

    @abstractmethod
    def saveVehicle(self, vehicle: Vehicle) -> Vehicle:
        pass

    @abstractmethod
    def findByLicensePlate(self, licensePlate: str) -> Optional[Vehicle]:
        pass

    @abstractmethod
    def getVehicleType(self, id: VehicleId) -> VehicleType:
        pass

