from datetime import datetime
from typing import Optional, List, cast

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.ports.ReservationRepository import ReservationRepository
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationData import ReservationData
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationMapper import ReservationMapper
from src.shared.error.CustomException import CustomException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.ErrorType import ErrorType
from src.shared.error.enums.InfrastructureErrorType import InfrastructureErrorType


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
            self.__handleSqlalchemyException(session, exc)
        finally:
            session.close()

    def findById(self, reservationId: ReservationId) -> Optional[Reservation]:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData: Optional[ReservationData] = session.query(ReservationData).filter(
                ReservationData.id == reservationId.getValue()
            ).first()

            if reservationData is None:
                ExceptionHandler.raiseException(CustomException(
                    ErrorType.INFRASTRUCTURE_ERROR,
                    InfrastructureErrorType.RESERVATION_NOT_FOUND.name,
                    InfrastructureErrorType.RESERVATION_NOT_FOUND.value
                ))

            return ReservationMapper.toDomain(reservationData)
        except SQLAlchemyError as exc:
            self.__handleSqlalchemyException(session, exc)
        finally:
            session.close()

    def getReservationsByUserId(self, userId: UserId) -> Optional[List[Reservation]]:
        session: Session = self.__databaseService.getSession()
        try:
            reservationDataList = cast(List[ReservationData], session.query(ReservationData).filter(
                ReservationData.user_id == userId.getValue()
            ).all())
            return [
                ReservationMapper.toDomain(reservationData)
                for reservationData in reservationDataList
            ]
        except SQLAlchemyError as exc:
            self.__handleSqlalchemyException(session, exc)
        finally:
            session.close()

    def getAllReservations(self) -> Optional[List[Reservation]]:
        session: Session = self.__databaseService.getSession()
        try:
            reservationDataList = cast(List[ReservationData], session.query(ReservationData).all())
            return [
                ReservationMapper.toDomain(reservationData)
                for reservationData
                in reservationDataList
            ]
        except SQLAlchemyError as exc:
            self.__handleSqlalchemyException(session, exc)
        finally:
            session.close()

    def updateStatus(self, reservationId: ReservationId, status: ReservationStatus) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData = session.query(ReservationData).filter(
                ReservationData.id == reservationId.getValue()
            ).first()
            reservationData.status = status.getValue()
            session.commit()
        except SQLAlchemyError as exc:
            self.__handleSqlalchemyException(session, exc)
        finally:
            session.close()

    def updateEndTime(self, reservationId: ReservationId, endTime: datetime) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData = session.query(ReservationData).filter(
                ReservationData.id == reservationId.getValue()
            ).first()
            reservationData.end_time = endTime
            session.commit()
        except SQLAlchemyError as exc:
            self.__handleSqlalchemyException(session, exc)
        finally:
            session.close()

    def updateStarTime(self, reservationId: ReservationId, startTime: datetime) -> None:
        session: Session = self.__databaseService.getSession()
        try:
            reservationData = session.query(ReservationData).filter(
                ReservationData.id == reservationId.getValue()
            ).first()
            reservationData.start_time = startTime
            session.commit()
        except SQLAlchemyError as exc:
            self.__handleSqlalchemyException(session, exc)
        finally:
            session.close()

    @staticmethod
    def __handleSqlalchemyException(session: Session, exc: SQLAlchemyError) -> None:
        session.rollback()
        ExceptionHandler.raiseException(CustomException(
            ErrorType.INFRASTRUCTURE_ERROR,
            InfrastructureErrorType.DATABASE_ERROR.name,
            InfrastructureErrorType.DATABASE_ERROR.value,
            {"original_error": str(exc)}
        ))
