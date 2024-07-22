from src.domain.models.vehicle_type.value_objects.VehicleTypeId import VehicleTypeId
from src.domain.models.vehicle_type.value_objects.VehicleTypeName import VehicleTypeName


class VehicleType:

    __id: VehicleTypeId
    __typeName: VehicleTypeName

    def __init__(self,
                 id: VehicleTypeId,
                 typeName: VehicleTypeName
                 ):
        self.__id = id
        self.__typeName = typeName

    def getId(self) -> VehicleTypeId:
        return self.__id

    def getTypeName(self) -> VehicleTypeName:
        return self.__typeName
