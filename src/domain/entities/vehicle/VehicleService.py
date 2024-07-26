from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.VehicleFactory import VehicleFactory
from src.domain.entities.vehicle.ports.VehicleGateway import VehicleGateway
from src.domain.entities.vehicle.ports.VehicleRepository import VehicleRepository
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class VehicleService(VehicleGateway):

    __vehicleRepository: VehicleRepository

    def __init__(self, outputAdapter: VehicleRepository):
        self.__vehicleRepository = outputAdapter

    def createVehicle(self,
                      userId: UserId,
                      licensePlate: str,
                      model: str,
                      vehicleType: VehicleType) -> Vehicle:

        newVehicle: Vehicle = VehicleFactory.create(
            userId=userId,
            licensePlate=licensePlate,
            model=model,
            vehicleType=vehicleType
        )
        self.__vehicleRepository.saveVehicle(newVehicle)
        return newVehicle
