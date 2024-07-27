from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.ports.VehicleRepository import VehicleRepository
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.common.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.vehicle_data.VehicleData import VehicleData
from src.infrastructure.output_adapters.persistence.entities.vehicle_data.VehicleMapper import VehicleMapper
from src.shared.utils.ErrorHandler import CustomException, ErrorType, ExceptionHandler


class VehiclePostgreRepository(VehicleRepository):

    __databaseService: DatabaseService

    def __init__(self, adapterService: DatabaseService):
        self.__databaseService = adapterService

    def saveVehicle(self, vehicle: Vehicle) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            vehicleData: VehicleData = VehicleMapper.toPersistence(vehicle)
            session.add(vehicleData)
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