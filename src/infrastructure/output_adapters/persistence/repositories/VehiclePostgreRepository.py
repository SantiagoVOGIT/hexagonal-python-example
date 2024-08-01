from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.ports.VehicleRepository import VehicleRepository
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.infrastructure.common.DatabaseService import DatabaseService
from src.shared.error.CustomException import CustomException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.ErrorType import ErrorType
from src.shared.error.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.vehicle_data.VehicleData import VehicleData
from src.infrastructure.output_adapters.persistence.entities.vehicle_data.VehicleMapper import VehicleMapper


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

    def findByLicensePlate(self, licensePlate: str) -> Optional[Vehicle]:
        session: Session = self.__databaseService.getSession()
        try:
            vehicleData: Optional[VehicleData] = session.query(VehicleData).filter_by(
                license_plate=licensePlate
            ).first()
            if vehicleData is None:
                return None
            return VehicleMapper.toDomain(vehicleData)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def getVehicleType(self, vehicleId: VehicleId) -> VehicleType:
        session: Session = self.__databaseService.getSession()
        try:
            vehicleData = session.query(VehicleData).filter(
                VehicleData.id == vehicleId.getValue()
            ).first()
            if vehicleData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.INFRASTRUCTURE_ERROR,
                    InfrastructureErrorType.VEHICLE_NOT_FOUND.name,
                    InfrastructureErrorType.VEHICLE_NOT_FOUND.value
                ))
            return VehicleType(vehicleData.vehicle_type)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()

    def updateVehicle(self, vehicle: Vehicle) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            vehicleData = session.query(VehicleData).filter(
                VehicleData.id == vehicle.getId().getValue()
            ).first()

            vehicleData.user_id = vehicle.getUserId().getValue()
            vehicleData.license_plate = vehicle.getLicensePlate()
            vehicleData.model = vehicle.getModel()
            vehicleData.vehicle_type = vehicle.getVehicleType().getValue()

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

    def findById(self, vehicleId: VehicleId) -> Optional[Vehicle]:
        session: Session = self.__databaseService.getSession()
        try:
            vehicleData: Optional[VehicleData] = session.query(VehicleData).filter(
                VehicleData.id == vehicleId.getValue()
            ).first()

            if vehicleData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.INFRASTRUCTURE_ERROR,
                    InfrastructureErrorType.VEHICLE_NOT_FOUND.name,
                    InfrastructureErrorType.VEHICLE_NOT_FOUND.value
                ))
            return VehicleMapper.toDomain(vehicleData)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()
