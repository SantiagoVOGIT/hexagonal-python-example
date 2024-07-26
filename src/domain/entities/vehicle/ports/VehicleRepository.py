from abc import ABC, abstractmethod

from src.domain.entities.vehicle.Vehicle import Vehicle


class VehicleRepository(ABC):

    @abstractmethod
    def saveVehicle(self, vehicle: Vehicle) -> Vehicle:
        pass
