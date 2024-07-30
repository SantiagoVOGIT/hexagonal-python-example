from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.cell.ports.CellGateway import CellGateway
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.CellDTO import CellDTO
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class CellController:

    cellGateway: CellGateway

    def __init__(self, useCase: CellGateway):
        self.cellGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/create-cell")
        async def createReservation(request: CellDTO):
            try:
                self.cellGateway.createCell(
                    request.spaceNumber,
                    request.vehicleType,
                    request.status
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCES_CREATED_CELL)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )
