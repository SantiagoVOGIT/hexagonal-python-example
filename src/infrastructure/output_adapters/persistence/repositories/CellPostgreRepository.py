from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.ports.CellRepository import CellRepository
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.common.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.cell_data.CellData import CellData
from src.infrastructure.output_adapters.persistence.entities.cell_data.CellMapper import CellMapper
from src.shared.utils.ErrorHandler import ExceptionHandler, CustomException, ErrorType


class CellPostgreRepository(CellRepository):

    __databaseService: DatabaseService

    def __init__(self, adapterService: DatabaseService):
        self.__databaseService = adapterService

    def saveCell(self, cell: Cell) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            cellData: CellData = CellMapper.toPersistence(cell)
            session.add(cellData)
            session.commit()
        except SQLAlchemyError as exc:
            session.rollback()
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()
