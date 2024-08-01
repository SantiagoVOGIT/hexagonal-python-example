from typing import Optional

from src.shared.error.DomainException import DomainException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.DomainErrorType import DomainErrorType
from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.CellFactory import CellFactory
from src.domain.entities.cell.ports.CellRepository import CellRepository
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.domain.entities.cell.ports.CellGateway import CellGateway


class CellUseCase(CellGateway):

    __cellRepository: CellRepository

    def __init__(self, cellOutputAdapter: CellRepository):
        self.__cellRepository = cellOutputAdapter

    def createCell(self,
                   spaceNumber: SpaceNumber,
                   vehicleType: VehicleType,
                   status: CellStatus
                   ) -> Cell:

        self.__validateNewSpaceNumber(spaceNumber)

        newCell: Cell = CellFactory.create(
            spaceNumber=spaceNumber,
            vehicleType=vehicleType,
            status=status
        )
        self.__cellRepository.saveCell(newCell)
        return newCell

    def updateCell(self,
                   cellId: CellId,
                   spaceNumber: SpaceNumber,
                   vehicleType: VehicleType,
                   status: CellStatus
                   ) -> Cell:

        cell: Optional[Cell] = self.__cellRepository.findById(cellId)
        currentSpaceNumber: str = cell.getSpaceNumber().getValue()

        if currentSpaceNumber != spaceNumber:
            self.__validateNewSpaceNumber(spaceNumber)

        updatedCell: Cell = CellFactory.update(
            cell=cell,
            spaceNumber=spaceNumber,
            vehicleType=vehicleType,
            status=status
        )
        self.__cellRepository.updateCell(updatedCell)
        return updatedCell

    def __validateNewSpaceNumber(self, spaceNumber: SpaceNumber):
        existingSpaceNumber: Optional[Cell] = self.__cellRepository.finBySpaceNumber(spaceNumber)
        if existingSpaceNumber is not None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.SPACE_NUMBER_ALREADY_EXISTS
            ))
