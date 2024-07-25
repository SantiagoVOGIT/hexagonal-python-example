from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationCode import ReservationCode
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationData import ReservationData


class ReservationMapper:

    @staticmethod
    def toDomain(reservationData: ReservationData) -> Reservation:
        return Reservation(
            id=ReservationId(reservationData.id),
            userId=UserId(reservationData.user_id),
            cellId=CellId(reservationData.cell_id),
            vehicleId=VehicleId(reservationData.vehicle_id),
            reservationCode=ReservationCode(reservationData.reservation_code),
            status=ReservationStatus(reservationData.status),
            startTime=reservationData.start_time,
            endTime=reservationData.end_time,
            createdAt=reservationData.created_at
        )

    @staticmethod
    def toPersistence(reservation: Reservation) -> ReservationData:
        return ReservationData(
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
