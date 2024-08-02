from typing import Optional, List

from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.VehicleFactory import VehicleFactory
from src.domain.entities.vehicle.ports.VehicleGateway import VehicleGateway
from src.domain.entities.vehicle.ports.VehicleRepository import VehicleRepository
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.shared.error.DomainException import DomainException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.DomainErrorType import DomainErrorType


class VehicleUseCase(VehicleGateway):

    __vehicleRepository: VehicleRepository

    def __init__(self, vehicleOutputAdapter):
        self.__vehicleRepository = vehicleOutputAdapter

    def createVehicle(self,
                      userId: UserId,
                      licensePlate: str,
                      model: str,
                      vehicleType: VehicleType
                      ) -> Vehicle:

        self.__validateUserId(userId)
        self.__validateNewLicensePlate(licensePlate)

        newVehicle: Vehicle = VehicleFactory.create(
            userId=userId,
            licensePlate=licensePlate,
            model=model,
            vehicleType=vehicleType
        )
        self.__vehicleRepository.saveVehicle(newVehicle)
        return newVehicle

    def updateVehicle(self,
                      vehicleId: VehicleId,
                      userId: Optional[UserId] = None,
                      licensePlate: Optional[str] = None,
                      model: Optional[str] = None,
                      vehicleType: Optional[VehicleType] = None,
                      ) -> Vehicle:

        vehicle: Optional[Vehicle] = self.__vehicleRepository.findById(vehicleId)
        currentLicensePlate: str = vehicle.getLicensePlate()

        if currentLicensePlate != licensePlate:
            self.__validateNewLicensePlate(licensePlate)

        updateVehicle: Vehicle = VehicleFactory.update(
            vehicle=vehicle,
            userId=userId,
            licensePlate=licensePlate,
            model=model,
            vehicleType=vehicleType
        )
        self.__vehicleRepository.updateVehicle(updateVehicle)
        return updateVehicle

    def getVehiclesByUserId(self, userId: UserId) -> List[Vehicle]:
        self.__validateUserId(userId)
        vehicles: Optional[List[Vehicle]] = self.__vehicleRepository.getVehiclesByUserId(userId)
        if not vehicles:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.VEHICLES_NOT_FOUND
            ))
        return vehicles

    def __validateNewLicensePlate(self, licensePlate: str):
        vehicle: Optional[Vehicle] = self.__vehicleRepository.findByLicensePlate(licensePlate)
        if vehicle is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.VEHICLE_ALREADY_EXISTS
            ))
        return vehicle

    @staticmethod
    def __validateUserId(userId: UserId) -> None:
        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))
