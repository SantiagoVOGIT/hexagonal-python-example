from datetime import datetime
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.ports.ReservationRepository import ReservationRepository
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.common.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationData import ReservationData
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationMapper import ReservationMapper
from src.shared.utils.ErrorHandler import ExceptionHandler, CustomException, ErrorType


class ReservationPostgreRepository(ReservationRepository):

    __databaseService: DatabaseService

    def __init__(self, adapterService: DatabaseService):
        self.__databaseService = adapterService

    def saveReservation(self, reservation: Reservation) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData: ReservationData = ReservationMapper.toPersistence(reservation)
            session.add(reservationData)
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

    def updateStatus(self, reservationId: ReservationId, status: ReservationStatus) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData = session.query(ReservationData).filter(
                ReservationData.id == str(reservationId)
            ).first()
            if reservationData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.DOMAIN_ERROR,
                    DomainErrorType.RESERVATION_NOT_FOUND.name,
                    DomainErrorType.RESERVATION_NOT_FOUND.value
                ))
            reservationData.status = status.value
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

    def updateEndTime(self, reservationId: ReservationId, endTime: datetime) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData = session.query(ReservationData).filter(
                ReservationData.id == str(reservationId)
            ).first()
            if reservationData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.DOMAIN_ERROR,
                    DomainErrorType.RESERVATION_NOT_FOUND.name,
                    DomainErrorType.RESERVATION_NOT_FOUND.value
                ))
            reservationData.end_time = endTime
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

    def updateStarTime(self, reservationId: ReservationId, startTime: datetime) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData = session.query(ReservationData).filter(
                ReservationData.id == str(reservationId)
            ).first()
            if reservationData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.DOMAIN_ERROR,
                    DomainErrorType.RESERVATION_NOT_FOUND.name,
                    DomainErrorType.RESERVATION_NOT_FOUND.value
                ))
            reservationData.start_time = startTime
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

    def getReservationById(self, reservationId: ReservationId) -> Optional[Reservation]:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData: Optional[ReservationData] = session.query(ReservationData).filter(
                ReservationData.id == reservationId.getValue()
            ).first()

            if reservationData is None:
                return None

            return ReservationMapper.toDomain(reservationData)
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.DATABASE_ERROR.name,
                InfrastructureErrorType.DATABASE_ERROR.value,
                {"original_error": str(exc)}
            ))
        finally:
            session.close()
