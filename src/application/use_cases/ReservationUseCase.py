from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.ReservationFactory import ReservationFactory
from src.domain.entities.reservation.ports.ReservationRepository import ReservationRepository
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.input_ports.ReservationGateway import ReservationGateway
from src.shared.utils.ErrorHandler import ExceptionHandler, DomainException


class ReservationUseCase(ReservationGateway):

    __reservationRepository: ReservationRepository

    def __init__(self, outputAdapter: ReservationRepository):
        self.__reservationRepository = outputAdapter

    def createReservation(self,
                          userId: UserId,
                          cellId: CellId,
                          vehicleId: VehicleId
                          ) -> Reservation:

        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))

        newReservation: Reservation = ReservationFactory.create(
            userId=userId,
            cellId=cellId,
            vehicleId=vehicleId,
            status=ReservationStatus.PENDING
        )
        self.__reservationRepository.saveReservation(newReservation)
        return newReservation
