from datetime import datetime
from typing import Optional

from src.domain.common.DomainUtils import DomainUtils
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.reservation.value_objects.ReservationCode import ReservationCode
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.domain.entities.reservation.value_objects.ReservationStatus import ReservationStatus
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId


class Reservation:

    __id: ReservationId
    __userId: UserId
    __cellId: CellId
    __vehicleId: VehicleId
    __reservationCode: ReservationCode
    __status: ReservationStatus
    __startTime: datetime
    __endTime: datetime
    __createdAt: datetime

    def __init__(self,
                 userId: UserId,
                 cellId: CellId,
                 vehicleId: VehicleId,
                 reservationCode: Optional[ReservationCode] = None,
                 status: ReservationStatus = ReservationStatus.PENDING,
                 startTime: Optional[datetime] = None,
                 endTime: Optional[datetime] = None,
                 id: Optional[ReservationId] = None,
                 createAt: Optional[datetime] = None
                 ):
        self.__id = DomainUtils.resolveId(id, ReservationId)
        self.__userId = userId
        self.__cellId = cellId
        self.__vehicleId = vehicleId
        self.__reservationCode = Reservation.__resolveReservationCode(reservationCode)
        self.__status = status
        self.__startTime = DomainUtils.resolveCreatedAt(startTime)
        self.__endTime = endTime
        self.__createdAt = DomainUtils.resolveCreatedAt(createAt)

    def getId(self) -> ReservationId:
        return self.__id

    def getUserId(self) -> UserId:
        return self.__userId

    def getCellId(self) -> CellId:
        return self.__cellId

    def getVehicleId(self) -> VehicleId:
        return self.__vehicleId

    def getReservationCode(self) -> ReservationCode:
        return self.__reservationCode

    def getStatus(self) -> ReservationStatus:
        return self.__status

    def getStartTime(self) -> datetime:
        return self.__startTime

    def getEndTime(self) -> datetime:
        return self.__endTime

    def getCreatedAt(self) -> datetime:
        return self.__createdAt

    @staticmethod
    def __resolveReservationCode(reservationCode) -> ReservationCode:
        return reservationCode if reservationCode is not None else ReservationCode.generate()
