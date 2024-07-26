from abc import ABC, abstractmethod

from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class VehicleGateway(ABC):

    @abstractmethod
    def createVehicle(self,
                      userId: UserId,
                      licensePlate: str,
                      model: str,
                      vehicleType: VehicleType) -> Vehicle:
        pass