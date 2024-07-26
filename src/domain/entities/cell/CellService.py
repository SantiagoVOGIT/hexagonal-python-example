from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.CellFactory import CellFactory
from src.domain.entities.cell.ports.CellGateway import CellGateway
from src.domain.entities.cell.ports.CellRepository import CellRepository
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


class CellService(CellGateway):

    cellRepository: CellRepository

    def __init__(self, outputAdapter: CellRepository):
        self.cellRepository = outputAdapter

