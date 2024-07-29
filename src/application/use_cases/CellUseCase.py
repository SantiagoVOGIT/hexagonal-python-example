from typing import Optional

from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.CellFactory import CellFactory
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.input_ports.CellGateway import CellGateway
from src.domain.entities.cell.ports.CellRepository import CellRepository
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.shared.utils.ErrorHandler import DomainException, ExceptionHandler


class CellUseCase(CellGateway):

    __cellRepository: CellRepository

    def __init__(self, cellOutputAdapter: CellRepository):
        self.__cellRepository = cellOutputAdapter

    def createCell(self,
                   spaceNumber: SpaceNumber,
                   vehicleType: VehicleType,
                   status: CellStatus
                   ) -> Cell:

        existingCell: Optional[Cell] = self.__cellRepository.finBySpaceNumber(spaceNumber)
        if existingCell is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.CELL_ALREADY_EXISTS,
                {"spaceNumber": spaceNumber}
            ))

        newCell: Cell = CellFactory.create(
            spaceNumber=spaceNumber,
            vehicleType=vehicleType,
            status=status
        )
        self.__cellRepository.saveCell(newCell)
        return newCell

