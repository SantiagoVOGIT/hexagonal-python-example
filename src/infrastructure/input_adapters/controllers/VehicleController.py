from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.vehicle.ports.VehicleGateway import VehicleGateway
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.VehicleDTO import VehicleDTO
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class VehicleController:

    __vehicleGateway: VehicleGateway

    def __init__(self, useCase: VehicleGateway):
        self.__vehicleGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/create-vehicle")
        async def createReservation(request: VehicleDTO):
            try:
                self.__vehicleGateway.createVehicle(
                    request.userId,
                    request.licensePlate,
                    request.model,
                    request.vehicleType
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCES_CREATED_VEHICLE)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )
