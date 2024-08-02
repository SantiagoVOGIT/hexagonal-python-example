from datetime import datetime
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationCode import ReservationCode
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.shared.decorators.UtilityClass import utilityClass


@utilityClass
class ReservationFactory:

    @staticmethod
    def create(userId: UserId,
               cellId: CellId,
               vehicleId: VehicleId,
               status: ReservationStatus,
               endTime: Optional[datetime] = None,
               startTime: Optional[datetime] = None,
               reservationCode: Optional[ReservationCode] = None,
               id: Optional[ReservationId] = None,
               createdAt: Optional[datetime] = None
               ) -> Reservation:

        return Reservation(
            userId=userId,
            cellId=cellId,
            vehicleId=vehicleId,
            endTime=endTime,
            startTime=startTime,
            status=status,
            reservationCode=DomainUtils.resolveReservationCode(reservationCode),
            id=DomainUtils.resolveId(id, ReservationId),
            createdAt=DomainUtils.resolveCreatedAt(createdAt),
        )
