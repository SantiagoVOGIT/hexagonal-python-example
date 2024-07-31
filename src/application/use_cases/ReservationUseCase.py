from datetime import datetime, timezone
from typing import List, Optional

from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.cell.ports.CellRepository import CellRepository
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.ReservationFactory import ReservationFactory
from src.domain.entities.reservation.ports.ReservationGateway import ReservationGateway
from src.domain.entities.reservation.ports.ReservationRepository import ReservationRepository
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.ports.VehicleRepository import VehicleRepository
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.shared.utils.ErrorHandler import ExceptionHandler, DomainException


class ReservationUseCase(ReservationGateway):

    __reservationRepository: ReservationRepository
    __cellRepository: CellRepository
    __vehicleRepository: VehicleRepository

    def __init__(self,
                 reservationOutputAdapter: ReservationRepository,
                 cellOutputAdapter: CellRepository,
                 vehicleOutputAdapter: VehicleRepository
                 ):
        self.__reservationRepository = reservationOutputAdapter
        self.__cellRepository = cellOutputAdapter
        self.__vehicleRepository = vehicleOutputAdapter

    def createReservation(self,
                          userId: UserId,
                          cellId: CellId,
                          vehicleId: VehicleId
                          ) -> Reservation:

        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))

        cellStatus = self.__cellRepository.getStatus(cellId)
        if cellStatus != CellStatus.AVAILABLE:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.CELL_NOT_AVAILABLE,
            ))

        userVehicleType = self.__vehicleRepository.getVehicleType(vehicleId)
        cellVehicleType = self.__cellRepository.getVehicleType(cellId)
        if userVehicleType != cellVehicleType:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INCOMPATIBLE_VEHICLE_TYPE_CELL
            ))

        newReservation: Reservation = ReservationFactory.create(
            userId=userId,
            cellId=cellId,
            vehicleId=vehicleId,
            status=ReservationStatus.PENDING
        )
        self.__reservationRepository.saveReservation(newReservation)
        self.__cellRepository.updateStatus(cellId, CellStatus.RESERVED)
        return newReservation

    def cancelReservation(self, reservationId: ReservationId) -> None:
        reservation = self.__reservationRepository.findById(reservationId)
        if reservation is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATION_NOT_FOUND
            ))

        endTime: datetime = datetime.now(timezone.utc)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.CANCELLED)
        self.__reservationRepository.updateEndTime(reservationId, endTime)

        cellId = reservation.getCellId()
        self.__cellRepository.updateStatus(cellId, CellStatus.AVAILABLE)

    def rejectReservation(self, reservationId: ReservationId) -> None:
        reservation = self.__reservationRepository.findById(reservationId)
        if reservation is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATION_NOT_FOUND
            ))

        endTime: datetime = datetime.now(timezone.utc)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.REJECTED)
        self.__reservationRepository.updateEndTime(reservationId, endTime)

        cellId = reservation.getCellId()
        self.__cellRepository.updateStatus(cellId, CellStatus.AVAILABLE)

    def confirmReservation(self, reservationId: ReservationId) -> None:
        reservation = self.__reservationRepository.findById(reservationId)
        if reservation is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATION_NOT_FOUND
            ))

        startTime: datetime = datetime.now(timezone.utc)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.CONFIRMED)
        self.__reservationRepository.updateStarTime(reservationId, startTime)

        cellId = reservation.getCellId()
        self.__cellRepository.updateStatus(cellId, CellStatus.OCCUPIED)

    def completeReservation(self, reservationId: ReservationId) -> None:
        reservation = self.__reservationRepository.findById(reservationId)
        if reservation is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATION_NOT_FOUND
            ))

        endTime: datetime = datetime.now(timezone.utc)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.COMPLETED)
        self.__reservationRepository.updateEndTime(reservationId, endTime)

        cellId = reservation.getCellId()
        self.__cellRepository.updateStatus(cellId, CellStatus.AVAILABLE)

    def getAllReservations(self) -> Optional[List[Reservation]]:
        reservations: Optional[List[Reservation]] = self.__reservationRepository.getAllReservations()
        if not reservations:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATIONS_NOT_FOUND
            ))
        return reservations

    def getReservationById(self, reservationId: ReservationId) -> Optional[Reservation]:
        reservation: Optional[Reservation] = self.__reservationRepository.findById(reservationId)
        if reservation is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATION_NOT_FOUND
            ))
        return reservation

