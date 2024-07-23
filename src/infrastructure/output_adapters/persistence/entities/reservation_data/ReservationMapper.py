from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationCode import ReservationCode
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationModel import ReservationModel


class ReservationMapper:

    @staticmethod
    def toDomain(reservationModel: ReservationModel) -> Reservation:
        return Reservation(
            id=ReservationId(reservationModel.id),
            userId=UserId(reservationModel.user_id),
            cellId=CellId(reservationModel.cell_id),
            vehicleId=VehicleId(reservationModel.vehicle_id),
            reservationCode=ReservationCode(reservationModel.reservation_code),
            status=ReservationStatus(reservationModel.status),
            startTime=reservationModel.start_time,
            endTime=reservationModel.end_time,
            createdAt=reservationModel.created_at
        )

    @staticmethod
    def toPersistence(reservation: Reservation) -> ReservationModel:
        return ReservationModel(
            id=reservation.getId().getValue(),
            user_id=reservation.getUserId().getValue(),
            cell_id=reservation.getCellId().getValue(),
            vehicle_id=reservation.getVehicleId().getValue(),
            reservation_code=reservation.getReservationCode().getValue(),
            status=reservation.getStatus().getValue(),
            start_time=reservation.getStartTime(),
            end_time=reservation.getEndTime(),
            created_at=reservation.getCreatedAt()
        )
