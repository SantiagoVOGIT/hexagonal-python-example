from abc import ABC, abstractmethod
from src.domain.entities.reservation.Reservation import Reservation


class ReservationRepository(ABC):

    @abstractmethod
    def saveReservation(self, reservation: Reservation) -> Reservation:
        pass

