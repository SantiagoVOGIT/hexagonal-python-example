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
               id: Optional[VehicleId] = None) -> Vehicle:

        return Vehicle(
            userId=userId,
            model=model,
            licensePlate=DomainUtils.validateLicensePlate(licensePlate),
            vehicleType=DomainUtils.validateEnum(vehicleType, VehicleType),
            id=DomainUtils.resolveId(id, VehicleId),
            registeredAt=DomainUtils.resolveCreatedAt(registeredAt)
        )
