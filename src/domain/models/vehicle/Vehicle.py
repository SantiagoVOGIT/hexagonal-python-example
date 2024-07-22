from datetime import datetime
from typing import Optional

from src.domain.models.user.value_objects.UserId import UserId
from src.domain.models.vehicle.value_objects.LicensePlate import LicensePlate
from src.domain.models.vehicle.value_objects.VehicleId import VehicleId
from src.domain.models.vehicle_type.value_objects.VehicleTypeId import VehicleTypeId


class Vehicle:

    __id: VehicleId
    __userId: UserId
    __licensePlate: LicensePlate
    __model: str
    __vehicleTypeId: VehicleTypeId
    __registeredAt: datetime

    def __init__(self,
                 id: VehicleId,
                 userId: UserId,
                 licensePlate: LicensePlate,
                 model: str,
                 vehicleTypeId: VehicleTypeId,
                 registeredAt: Optional[datetime] = None
                 ):
        self.__id = id
        self.__userId = userId
        self.__licensePlate = licensePlate
        self.__model = model
        self.__vehicleTypeId = vehicleTypeId
        self.__registeredAt = Vehicle.__resolveRegisteredAt(registeredAt)

    def getId(self) -> VehicleId:
        return self.__id

    def getUserId(self) -> UserId:
        return self.__userId

    def getLicensePlate(self) -> LicensePlate:
        return self.__licensePlate

    def getModel(self) -> str:
        return self.__model

    def getVehicleTypeId(self) -> VehicleTypeId:
        return self.__vehicleTypeId

    def getRegisteredAt(self) -> datetime:
        return self.__registeredAt

    @staticmethod
    def __resolveRegisteredAt(registeredAt: Optional[datetime] = None) -> datetime:
        return registeredAt if registeredAt else datetime.now()


vehicle_id = VehicleId.generate()
user_id = UserId.generate()
vehicle_type_id = VehicleTypeId.generate()
license_plate = LicensePlate("ABC123")
model = "Toyota Corolla"
registered_at = datetime(2023, 1, 1)

# 7. Crear una instancia de Vehicle
vehicle = Vehicle(
    id=vehicle_id,
    userId=user_id,
    licensePlate=license_plate,
    model=model,
    vehicleTypeId=vehicle_type_id,
    registeredAt=registered_at
)

print(vehicle.getLicensePlate().getValue())