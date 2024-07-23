from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.infrastructure.output_adapters.persistence.entities.cell_data.CellModel import CellModel


class CellMapper:

    @staticmethod
    def toDomain(cellModel: CellModel) -> Cell:
        return Cell(
            id=CellId(cellModel.id),
            spaceNumber=SpaceNumber(cellModel.space_number),
            vehicleType=VehicleType(cellModel.vehicle_type),
            status=CellStatus(cellModel.status),
            createdAt=cellModel.created_at
        )

    @staticmethod
    def toPersistence(cell: Cell) -> CellModel:
        return CellModel(
            id=cell.getId().getValue(),
            space_number=cell.getSpaceNumber().getValue(),
            vehicle_type=cell.getVehicleType().getValue(),
            status=cell.getStatus().getValue(),
            created_at=cell.getCreatedAt()
        )
