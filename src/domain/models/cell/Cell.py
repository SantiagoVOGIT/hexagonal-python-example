from datetime import datetime
from typing import Optional

from src.domain.models.cell.value_objects.CellId import CellId
from src.domain.models.cell.value_objects.CellStatus import CellStatus
from src.domain.models.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.models.vehicle_type.value_objects import VehicleTypeId


class Cell:

    __id: CellId
    __spaceNumber: SpaceNumber
    __vehicleTypeId: VehicleTypeId
    __status: CellStatus
    __createdAt: datetime

    def __init__(self,
                 id: CellId,
                 spaceNumber: SpaceNumber,
                 vehicleTypeId: VehicleTypeId,
                 status: CellStatus,
                 createdAt: Optional[datetime] = None
                 ):
        self.__id = id
        self.__spaceNumber = spaceNumber
        self.__vehicleTypeId = vehicleTypeId
        self.__status = status
        self.__createdAt = Cell.__resolveCreatedAt(createdAt)

    def getId(self) -> CellId:
        return self.__id

    def getSpaceNumber(self) -> SpaceNumber:
        return self.__spaceNumber

    def getVehicleTypeId(self) -> VehicleTypeId:
        return self.__vehicleTypeId

    def getStatus(self) -> CellStatus:
        return self.__status

    def getCreatedAt(self) -> datetime:
        return self.__createdAt

    @staticmethod
    def __resolveCreatedAt(createdAt: Optional[datetime] = None) -> datetime:
        return createdAt if createdAt else datetime.now()
