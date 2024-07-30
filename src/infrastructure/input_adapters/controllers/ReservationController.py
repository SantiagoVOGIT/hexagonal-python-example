from typing import Dict, Any, List, Optional

from fastapi import FastAPI, HTTPException

from src.domain.entities.reservation.Reservation import Reservation
from src.domain.entities.reservation.ports.ReservationGateway import ReservationGateway
from src.domain.entities.reservation.value_objects.ReservationId import ReservationId
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.ReservationDTO import ReservationDTO
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class ReservationController:

    __reservationGateway: ReservationGateway

    def __init__(self, useCase: ReservationGateway):
        self.__reservationGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/create-reservation")
        async def createReservation(request: ReservationDTO):
            try:
                self.__reservationGateway.createReservation(
                    request.userId,
                    request.cellId,
                    request.vehicleId
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_CREATED_RESERVATION)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )

        @app.post("/cancel-reservation")
        async def cancelReservation(request: ReservationDTO):
            try:
                self.__reservationGateway.cancelReservation(
                    request.reservationId
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_CANCEL_RESERVATION)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )

        @app.post("/reject-reservation")
        async def rejectReservation(request: ReservationDTO):
            try:
                self.__reservationGateway.cancelReservation(
                    request.reservationId
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_REJECT_RESERVATION)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )

        @app.post("/confirm-reservation")
        async def createReservation(request: ReservationDTO):
            try:
                self.__reservationGateway.confirmReservation(
                    request.reservationId,
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_CONFIRM_RESERVATION)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )

        @app.post("/complete-reservation")
        async def createReservation(request: ReservationDTO):
            try:
                self.__reservationGateway.completeReservation(
                    request.reservationId,
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_COMPLETE_RESERVATION)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )

        @app.get("/reservations")
        async def getAllReservations():
            try:
                reservations: Optional[List[Reservation]] = self.__reservationGateway.getAllReservations()
                return {
                    "reservations": [Reservation.toDict(reservation) for reservation in reservations]
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )

        @app.get("/reservation/{reservation_id}")
        async def getReservationById(reservation_id: str):
            try:
                reservationId = ReservationId(reservation_id)
                reservation = self.__reservationGateway.getReservationById(reservationId)
                return {
                    "reservation": Reservation.toDict(reservation)
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )
