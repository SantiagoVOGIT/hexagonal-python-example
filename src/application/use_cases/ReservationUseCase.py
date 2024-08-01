from datetime import datetime, timezone
from typing import List, Optional

from src.shared.error.DomainException import DomainException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.DomainErrorType import DomainErrorType
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
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType


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

    def createReservation(self, userId: UserId, cellId: CellId, vehicleId: VehicleId) -> Reservation:

        self.__validateUserId(userId)
        self.__validateCellAvailability(cellId)
        self.__validateVehicleCompatibility(vehicleId, cellId)

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
        reservation: Optional[Reservation] = self.__reservationRepository.findById(reservationId)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.CANCELLED)
        self.__reservationRepository.updateEndTime(reservationId, datetime.now(timezone.utc))
        self.__cellRepository.updateStatus(reservation.getCellId(), CellStatus.AVAILABLE)

    def rejectReservation(self, reservationId: ReservationId) -> None:
        reservation: Optional[Reservation] = self.__reservationRepository.findById(reservationId)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.REJECTED)
        self.__reservationRepository.updateEndTime(reservationId, datetime.now(timezone.utc))
        self.__cellRepository.updateStatus(reservation.getCellId(), CellStatus.AVAILABLE)

    def confirmReservation(self, reservationId: ReservationId) -> None:
        reservation: Optional[Reservation] = self.__reservationRepository.findById(reservationId)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.CONFIRMED)
        self.__reservationRepository.updateStarTime(reservationId, datetime.now(timezone.utc))
        self.__cellRepository.updateStatus(reservation.getCellId(), CellStatus.OCCUPIED)

    def completeReservation(self, reservationId: ReservationId) -> None:
        reservation: Optional[Reservation] = self.__reservationRepository.findById(reservationId)
        self.__reservationRepository.updateStatus(reservationId, ReservationStatus.COMPLETED)
        self.__reservationRepository.updateEndTime(reservationId, datetime.now(timezone.utc))
        self.__cellRepository.updateStatus(reservation.getCellId(), CellStatus.AVAILABLE)

    def getAllReservations(self) -> List[Reservation]:
        reservations: Optional[List[Reservation]] = self.__reservationRepository.getAllReservations()
        if not reservations:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATIONS_NOT_FOUND
            ))
        return reservations

    def getReservationById(self, reservationId: ReservationId) -> Reservation:
        reservation: Optional[Reservation] = self.__reservationRepository.findById(reservationId)
        return reservation

    def getReservationsByUserId(self, userId: UserId) -> List[Reservation]:
        reservations: Optional[List[Reservation]] = self.__reservationRepository.getReservationsByUserId(userId)
        if not reservations:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.RESERVATIONS_NOT_FOUND
            ))
        return reservations

    def __validateCellAvailability(self, cellId: CellId) -> None:
        cellStatus: CellStatus = self.__cellRepository.getStatus(cellId)
        if cellStatus != CellStatus.AVAILABLE:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.CELL_NOT_AVAILABLE
            ))

    def __validateVehicleCompatibility(self, vehicleId: VehicleId, cellId: CellId) -> None:
        userVehicleType: VehicleType = self.__vehicleRepository.getVehicleType(vehicleId)
        cellVehicleType: VehicleType = self.__cellRepository.getVehicleType(cellId)
        if userVehicleType != cellVehicleType:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.INCOMPATIBLE_VEHICLE_TYPE_CELL
            ))

    @staticmethod
    def __validateUserId(userId: UserId) -> None:
        if userId is None:
            ExceptionHandler.raiseException(DomainException(
                DomainErrorType.USER_ID_REQUIRED,
            ))
