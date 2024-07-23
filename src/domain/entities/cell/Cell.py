from datetime import datetime, timezone
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class Cell:

    __id: CellId
    __spaceNumber: SpaceNumber
    __vehicleType: VehicleType
    __status: CellStatus
    __createdAt: datetime

    def __init__(self,
                 spaceNumber: SpaceNumber,
                 vehicleType: VehicleType,
                 status: CellStatus = CellStatus.AVAILABLE,
                 id: Optional[CellId] = None,
                 createdAt: Optional[datetime] = None
                 ):
        self.__id = DomainUtils.resolveId(id, CellId)
        self.__spaceNumber = spaceNumber
        self.__vehicleType = vehicleType
        self.__status = status
        self.__createdAt = DomainUtils.resolveCreatedAt(createdAt)

    def getId(self) -> CellId:
        return self.__id

    def getSpaceNumber(self) -> SpaceNumber:
        return self.__spaceNumber

    def getVehicleTypeId(self) -> VehicleType:
        return self.__vehicleType

    def getStatus(self) -> CellStatus:
        return self.__status

    def getCreatedAt(self) -> datetime:
        return self.__createdAt
