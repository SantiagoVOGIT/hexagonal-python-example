from src.domain.common.enums.DomainErrorType import DomainErrorType
from src.domain.entities.cell.ports.CellRepository import CellRepository
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.ReservationFactory import ReservationFactory
from src.domain.entities.reservation.ports.ReservationRepository import ReservationRepository
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.ports.VehicleRepository import VehicleRepository
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.input_ports.ReservationGateway import ReservationGateway
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
                {"status": f"{cellStatus.getValue()}"}
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
