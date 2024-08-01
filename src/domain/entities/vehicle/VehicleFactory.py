from datetime import datetime
from typing import Optional

from src.shared.decorators.UtilityClass import utilityClass
from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


@utilityClass
class VehicleFactory:

    @staticmethod
    def create(userId: UserId,
               licensePlate: str,
               model: str,
               vehicleType: VehicleType,
               registeredAt: Optional[datetime] = None,
               id: Optional[VehicleId] = None
               ) -> Vehicle:
        return Vehicle(
            userId=userId,
            model=DomainUtils.validateModel(model),
            licensePlate=DomainUtils.validateLicensePlate(licensePlate),
            vehicleType=DomainUtils.validateEnum(vehicleType, VehicleType),
            id=DomainUtils.resolveId(id, VehicleId),
            registeredAt=DomainUtils.resolveCreatedAt(registeredAt)
        )

    @staticmethod
    def update(vehicle: Vehicle,
               userId: Optional[UserId] = None,
               licensePlate: Optional[str] = None,
               model: Optional[str] = None,
               vehicleType: Optional[VehicleType] = None,
               registeredAt: Optional[datetime] = None
               ) -> Vehicle:
        return Vehicle(
            id=vehicle.getId(),
            userId=userId if userId is not None else vehicle.getUserId(),
            licensePlate=DomainUtils.validateLicensePlate(licensePlate) if licensePlate is not None else vehicle.getLicensePlate(),
            model=DomainUtils.validateModel(model) if model is not None else vehicle.getModel(),
            vehicleType=DomainUtils.validateEnum(vehicleType, VehicleType) if vehicleType is not None else vehicle.getVehicleType(),
            registeredAt=DomainUtils.resolveCreatedAt(registeredAt) if registeredAt is not None else vehicle.getRegisteredAt()
        )
