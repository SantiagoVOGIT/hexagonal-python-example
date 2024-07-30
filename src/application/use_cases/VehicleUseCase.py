from typing import Optional

from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.VehicleFactory import VehicleFactory
from src.domain.entities.vehicle.ports.VehicleRepository import VehicleRepository
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.domain.entities.vehicle.ports.VehicleGateway import VehicleGateway
from src.shared.utils.ErrorHandler import ExceptionHandler, DomainException


class VehicleUseCase(VehicleGateway):

    vehicleRepository: VehicleRepository

    def __init__(self, vehicleOutputAdapter):
        self.vehicleRepository = vehicleOutputAdapter

    def createVehicle(self,
                      userId: UserId,
                      licensePlate: str,
                      model: str,
                      vehicleType: VehicleType
                      ) -> Vehicle:

        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))

        existingVehicle: Optional[Vehicle] = self.vehicleRepository.findByLicensePlate(licensePlate)
        if existingVehicle is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.VEHICLE_ALREADY_EXISTS
            ))

        newVehicle: Vehicle = VehicleFactory.create(
            userId=userId,
            licensePlate=licensePlate,
            model=model,
            vehicleType=vehicleType
        )
        self.vehicleRepository.saveVehicle(newVehicle)
        return newVehicle
