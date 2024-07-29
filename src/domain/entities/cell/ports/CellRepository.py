from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class CellRepository(ABC):

    @abstractmethod
    def saveCell(self, cell: Cell) -> Cell:
        pass

    @abstractmethod
    def finBySpaceNumber(self, spaceNumber: SpaceNumber) -> Optional[Cell]:
        pass

    @abstractmethod
    def findById(self, id: CellId) -> Optional[Cell]:
        pass

    @abstractmethod
    def getStatus(self, id: CellId) -> CellStatus:
        pass

    @abstractmethod
    def getVehicleType(self, cellId: CellId) -> VehicleType:
        pass

    @abstractmethod
    def updateStatus(self, cellId: CellId, status: CellStatus) -> None:
        pass
