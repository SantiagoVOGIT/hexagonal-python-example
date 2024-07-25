from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from datetime import datetime

from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId

T = TypeVar('T')


class ReservationGateway(ABC):

    @abstractmethod
    def createReservation(self, userId: UserId, cellId: CellId, vehicleId: VehicleId) -> Reservation:

        pass

