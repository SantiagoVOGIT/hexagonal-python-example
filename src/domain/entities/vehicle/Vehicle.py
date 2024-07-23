from datetime import datetime
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class Vehicle:

    __id: VehicleId
    __userId: UserId
    __licensePlate: str
    __model: str
    __vehicleType: VehicleType
    __registeredAt: datetime

    def __init__(self,
                 userId: UserId,
                 licensePlate: str,
                 model: str,
                 vehicleType: VehicleType,
                 registeredAt: Optional[datetime] = None,
                 id: Optional[VehicleId] = None
                 ):
        self.__id = DomainUtils.resolveId(id, VehicleId)
        self.__userId = userId
        self.__licensePlate = DomainUtils.isValidLicensePlate(licensePlate)
        self.__model = model
        self.__vehicleType = vehicleType
        self.__registeredAt = DomainUtils.resolveCreatedAt(registeredAt)

    def getId(self) -> VehicleId:
        return self.__id

    def getUserId(self) -> UserId:
        return self.__userId

    def getLicensePlate(self) -> str:
        return self.__licensePlate

    def getModel(self) -> str:
        return self.__model

    def getVehicleTypeId(self) -> VehicleType:
        return self.__vehicleType

    def getRegisteredAt(self) -> datetime:
        return self.__registeredAt

