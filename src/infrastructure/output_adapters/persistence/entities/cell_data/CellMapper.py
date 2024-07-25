from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.infrastructure.output_adapters.persistence.entities.cell_data.CellData import CellData


class CellMapper:

    @staticmethod
    def toDomain(cellData: CellData) -> Cell:
        return Cell(
            id=CellId(cellData.id),
            spaceNumber=SpaceNumber(cellData.space_number),
            vehicleType=VehicleType(cellData.vehicle_type),
            status=CellStatus(cellData.status),
            createdAt=cellData.created_at
        )

    @staticmethod
    def toPersistence(cell: Cell) -> CellData:
        return CellData(
            id=cell.getId().getValue(),
            space_number=cell.getSpaceNumber().getValue(),
            vehicle_type=cell.getVehicleType().getValue(),
            status=cell.getStatus().getValue(),
            created_at=cell.getCreatedAt()
        )
