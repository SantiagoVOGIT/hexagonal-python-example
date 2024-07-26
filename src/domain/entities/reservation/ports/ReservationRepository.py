from abc import ABC, abstractmethod
from src.domain.entities.reservation.Reservation import Reservation


class ReservationRepository(ABC):

    @abstractmethod
    def save(self, reservation: Reservation) -> Reservation:
        pass

