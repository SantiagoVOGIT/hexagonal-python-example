from datetime import datetime
from typing import Dict, Any

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
                 id: CellId,
                 spaceNumber: SpaceNumber,
                 vehicleType: VehicleType,
                 status: CellStatus,
                 createdAt: datetime):
        self.__id = id
        self.__spaceNumber = spaceNumber
        self.__vehicleType = vehicleType
        self.__status = status
        self.__createdAt = createdAt

    def getId(self) -> CellId:
        return self.__id

    def getSpaceNumber(self) -> SpaceNumber:
        return self.__spaceNumber

    def getVehicleType(self) -> VehicleType:
        return self.__vehicleType

    def getStatus(self) -> CellStatus:
        return self.__status

    def getCreatedAt(self) -> datetime:
        return self.__createdAt

    @staticmethod
    def toDict(cell: 'Cell') -> Dict[str, Any]:
        return {
            "id": cell.getId().getValue(),
            "spaceNumber": cell.getSpaceNumber().getValue(),
            "vehicleType": cell.getVehicleType().value,
            "status": cell.getStatus().value,
            "createdAt": cell.getCreatedAt().isoformat()
        }
