from datetime import datetime
from typing import Optional

from src.common.decorators.UtilityClass import utilityClass
from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationCode import ReservationCode
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId


@utilityClass
class ReservationFactory:

    @staticmethod
    def create(userId: UserId,
               cellId: CellId,
               vehicleId: VehicleId,
               reservationCode: Optional[ReservationCode] = None,
               status: ReservationStatus = ReservationStatus.PENDING,
               startTime: Optional[datetime] = None,
               endTime: Optional[datetime] = None,
               id: Optional[ReservationId] = None,
               createdAt: Optional[datetime] = None) -> Reservation:

        ensureId = DomainUtils.resolveId(id, ReservationId)
        ensureStartTime = DomainUtils.resolveCreatedAt(startTime)
        ensureCreatedAt = DomainUtils.resolveCreatedAt(createdAt)
        ensureReservationCode = ReservationFactory.__resolveReservationCode(reservationCode)

        return Reservation(
            id=ensureId,
            userId=userId,
            cellId=cellId,
            vehicleId=vehicleId,
            reservationCode=ensureReservationCode,
            status=status,
            startTime=ensureStartTime,
            endTime=endTime,
            createdAt=ensureCreatedAt
        )

    @staticmethod
    def __resolveReservationCode(reservationCode: Optional[ReservationCode]) -> ReservationCode:
        return reservationCode if reservationCode is not None else ReservationCode.generate()


