from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.cell.Cell import Cell
from src.domain.entities.cell.ports.CellRepository import CellRepository
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
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

    def finBySpaceNumber(self, spaceNumber: SpaceNumber) -> Optional[Cell]:
        session: Session = self.__databaseService.getSession()
        try:
            spaceNumberData: Optional[CellData] = session.query(CellData).filter_by(
                space_number=spaceNumber
            ).first()
            if spaceNumberData is None:
                return None
            return CellMapper.toDomain(spaceNumberData)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def findById(self, id: CellId) -> Optional[Cell]:
        session: Session = self.__databaseService.getSession()
        try:
            cellIdData: Optional[CellData] = session.query(CellData).filter_by(
                id=id.getValue()
            ).first()
            if cellIdData is None:
                return None
            return CellMapper.toDomain(cellIdData)

        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def getStatus(self, cellId: CellId) -> CellStatus:
        session: Session = self.__databaseService.getSession()
        try:
            cellIdData = session.query(CellData).filter(CellData.id == str(cellId)).first()
            if cellIdData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.DOMAIN_ERROR,
                    DomainErrorType.CELL_NOT_FOUND.name,
                    DomainErrorType.CELL_NOT_FOUND.value
                ))
            return CellStatus(cellIdData.status)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def getVehicleType(self, id: CellId) -> VehicleType:
        session: Session = self.__databaseService.getSession()
        try:
            cellIdData = session.query(CellData).filter(CellData.id == str(id)).first()
            if cellIdData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.DOMAIN_ERROR,
                    DomainErrorType.CELL_NOT_FOUND.name,
                    DomainErrorType.CELL_NOT_FOUND.value
                ))
            return VehicleType(cellIdData.vehicle_type)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def updateStatus(self, id: CellId, status: CellStatus) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            cellData = session.query(CellData).filter(CellData.id == str(id)).first()
            if cellData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.DOMAIN_ERROR,
                    DomainErrorType.CELL_NOT_FOUND.name,
                    DomainErrorType.CELL_NOT_FOUND.value
                ))
            cellData.status = status.value
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
