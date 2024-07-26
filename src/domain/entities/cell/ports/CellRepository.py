from abc import ABC, abstractmethod
from src.domain.entities.cell.Cell import Cell


class CellRepository(ABC):

    @abstractmethod
    def saveCell(self, cell: Cell) -> Cell:
        pass
