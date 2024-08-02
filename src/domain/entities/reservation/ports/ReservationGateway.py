from abc import ABC, abstractmethod
from typing import TypeVar, List, Optional

from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId

T = TypeVar('T')


class ReservationGateway(ABC):

    @abstractmethod
    def createReservation(self,
                          userId: UserId,
                          cellId: CellId,
                          vehicleId: VehicleId
                          ) -> Reservation:
        pass

    @abstractmethod
    def getReservationById(self, reservationId: ReservationId) -> Optional[Reservation]:
        pass

    @abstractmethod
    def getReservationsByUserId(self, userId: UserId) -> List[Reservation]:
        pass

    @abstractmethod
    def getAllReservations(self) -> Optional[List[Reservation]]:
        pass

    @abstractmethod
    def cancelReservation(self, reservationId: ReservationId) -> None:
        pass

    @abstractmethod
    def rejectReservation(self, reservationId: ReservationId) -> None:
        pass

    @abstractmethod
    def confirmReservation(self, reservationId: ReservationId) -> None:
        pass

    @abstractmethod
    def completeReservation(self, reservationId: ReservationId) -> None:
        pass
