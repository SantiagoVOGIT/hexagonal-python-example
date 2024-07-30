from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List

from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus


class ReservationRepository(ABC):

    @abstractmethod
    def saveReservation(self, reservation: Reservation) -> Reservation:
        pass

    @abstractmethod
    def updateStatus(self, reservationId: ReservationId, status: ReservationStatus) -> None:
        pass

    @abstractmethod
    def updateEndTime(self, reservationId: ReservationId, endTime: datetime) -> None:
        pass

    @abstractmethod
    def updateStarTime(self, reservationId: ReservationId, startTime: datetime) -> None:
        pass

    @abstractmethod
    def getReservationById(self, reservationId: ReservationId) -> Optional[Reservation]:
        pass

    @abstractmethod
    def getAllReservations(self) -> Optional[List[Reservation]]:
        pass
