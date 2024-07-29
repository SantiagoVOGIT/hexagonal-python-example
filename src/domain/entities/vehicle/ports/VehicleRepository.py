from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.vehicle.Vehicle import Vehicle


class VehicleRepository(ABC):

    @abstractmethod
    def saveVehicle(self, vehicle: Vehicle) -> Vehicle:
        pass

    @abstractmethod
    def findByLicensePlate(self, licensePlate: str) -> Optional[Vehicle]:
        pass
