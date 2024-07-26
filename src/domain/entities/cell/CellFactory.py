from datetime import datetime
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.shared.decorators.UtilityClass import utilityClass


@utilityClass
class CellFactory:

    @staticmethod
    def create(spaceNumber: SpaceNumber,
               vehicleType: VehicleType,
               status: CellStatus,
               id: Optional[CellId] = None,
               createdAt: Optional[datetime] = None) -> Cell:

        return Cell(
            spaceNumber=DomainUtils.validateEnum(spaceNumber, SpaceNumber),
            vehicleType=DomainUtils.validateEnum(vehicleType, VehicleType),
            status=DomainUtils.validateEnum(status, CellStatus),
            id=DomainUtils.resolveId(id, CellId),
            createdAt=DomainUtils.resolveCreatedAt(createdAt),
        )

