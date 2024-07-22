from datetime import datetime
from typing import Optional

from src.domain.models.cell.value_objects.CellId import CellId
from src.domain.models.reservation.value_objects.ReservationCode import ReservationCode
from src.domain.models.reservation.value_objects.ReservationId import ReservationId
from src.domain.models.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.models.user.value_objects.UserId import UserId
from src.domain.models.vehicle.value_objects.VehicleId import VehicleId


class Reservation:

    __id: ReservationId
    __userId: UserId
    __cellId: CellId
    __vehicleId: VehicleId
    __status: ReservationStatus
    __reservationCode: ReservationCode
    __startTime: datetime
    __endTime: datetime
    __createdAt: datetime

    def __init__(self,
                 id: ReservationId,
                 userId: UserId,
                 cellId: CellId,
                 vehicleId: VehicleId,
                 status: ReservationStatus,
                 reservationCode: ReservationCode,
                 startTime: Optional[datetime] = None,
                 endTime: Optional[datetime] = None,
                 createdAt: Optional[datetime] = None
                 ):
        self.__id = id
        self.__userId = userId
        self.__cellId = cellId
        self.__vehicleId = vehicleId
        self.__status = status
        self.__reservationCode = reservationCode
        self.__startTime = startTime
        self.__endTime = endTime
        self.__createdAt = Reservation.__resolveCreatedAt(createdAt)

    def getId(self) -> ReservationId:
        return self.__id

    def getUserId(self) -> UserId:
        return self.__userId

    def getCellId(self) -> CellId:
        return self.__cellId

    def getVehicleId(self) -> VehicleId:
        return self.__vehicleId

    def getStatus(self) -> ReservationStatus:
        return self.__status

    def getReservationCode(self) -> ReservationCode:
        return self.__reservationCode

    def getStartTime(self) -> datetime:
        return self.__startTime

    def getEndTime(self) -> datetime:
        return self.__endTime

    def getCreatedAt(self) -> datetime:
        return self.__createdAt

    @staticmethod
    def __resolveCreatedAt(createdAt: Optional[datetime] = None) -> datetime:
        return createdAt if createdAt else datetime.now()
