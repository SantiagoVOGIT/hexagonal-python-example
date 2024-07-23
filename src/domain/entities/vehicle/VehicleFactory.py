from datetime import datetime
from typing import Optional

from src.common.decorators.UtilityClass import utilityClass
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

        ensureId = DomainUtils.resolveId(id, VehicleId)
        validatedLicensePlate = DomainUtils.isValidLicensePlate(licensePlate)
        ensureRegisteredAt = DomainUtils.resolveCreatedAt(registeredAt)

        return Vehicle(
            id=ensureId,
            userId=userId,
            licensePlate=validatedLicensePlate,
            model=model,
            vehicleType=vehicleType,
            registeredAt=ensureRegisteredAt
        )
