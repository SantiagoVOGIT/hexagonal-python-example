from datetime import datetime
from typing import Optional

from src.common.decorators.UtilityClass import utilityClass
from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


@utilityClass
class CellFactory:

    @staticmethod
    def create(spaceNumber: SpaceNumber,
               vehicleType: VehicleType,
               status: CellStatus = CellStatus.AVAILABLE,
               id: Optional[CellId] = None,
               createdAt: Optional[datetime] = None) -> Cell:

        ensureId = DomainUtils.resolveId(id, CellId)
        ensureCreatedAt = DomainUtils.resolveCreatedAt(createdAt)

        return Cell(
            id=ensureId,
            spaceNumber=spaceNumber,
            vehicleType=vehicleType,
            status=status,
            createdAt=ensureCreatedAt
        )

