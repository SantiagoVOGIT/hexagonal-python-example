from abc import ABC, abstractmethod
from typing import Optional

from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber


class CellRepository(ABC):

    @abstractmethod
    def saveCell(self, cell: Cell) -> Cell:
        pass

    @abstractmethod
    def finBySpaceNumber(self, spaceNumber: SpaceNumber) -> Optional[Cell]:
        pass
