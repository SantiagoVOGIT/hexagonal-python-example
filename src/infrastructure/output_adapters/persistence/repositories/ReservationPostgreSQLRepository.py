from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.ports.ReservationRepository import ReservationRepository
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.common.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationData import ReservationData
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationMapper import ReservationMapper
from src.shared.utils.ErrorHandler import ExceptionHandler, CustomException, ErrorType


class ReservationPostgreSQLRepository(ReservationRepository):

    __databaseService: DatabaseService

    def __init__(self, adapterService: DatabaseService):
        self.__databaseService = adapterService

    def save(self, reservation: Reservation) -> None:
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
