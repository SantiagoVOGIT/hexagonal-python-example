from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List

from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId


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
    def findById(self, reservationId: ReservationId) -> Optional[Reservation]:
        pass

    @abstractmethod
    def getAllReservations(self) -> Optional[List[Reservation]]:
        pass

    @abstractmethod
    def getReservationsByUserId(self, userId: UserId) -> Optional[List[Reservation]]:
        pass