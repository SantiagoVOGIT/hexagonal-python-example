from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from src.domain.entities.reservation.Reservation import Reservation
from src.domain.input_ports.ReservationGateway import ReservationGateway
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.ReservationDTO import ReservationDTO
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory
from src.domain.entities.cell.value_objects.CellId import CellId
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId

class ReservationController:

    __reservationGateway: ReservationGateway

    def __init__(self, useCase: ReservationGateway):
        self.__reservationGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:
        @app.post("/reserve")
        async def createReservation(request: ReservationDTO):
            try:
                reservation: Reservation = self.__reservationGateway.createReservation(
                    request.userId,
                    request.cellId,
                    request.vehicleId
                )
                return {
                    "detail": MessageFactory.build(InfrastructureInfo.SUCCESS_CREATED_RESERVATION).getDetail(),
                    "reservation": reservation.getReservationCode()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )