from datetime import datetime

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
                 id: VehicleId,
                 userId: UserId,
                 licensePlate: str,
                 model: str,
                 vehicleType: VehicleType,
                 registeredAt: datetime):
        self.__id = id
        self.__userId = userId
        self.__licensePlate = licensePlate
        self.__model = model
        self.__vehicleType = vehicleType
        self.__registeredAt = registeredAt

    def getId(self) -> VehicleId:
        return self.__id

    def getUserId(self) -> UserId:
        return self.__userId

    def getLicensePlate(self) -> str:
        return self.__licensePlate

    def getModel(self) -> str:
        return self.__model

    def getVehicleType(self) -> VehicleType:
        return self.__vehicleType

    def getRegisteredAt(self) -> datetime:
        return self.__registeredAt
