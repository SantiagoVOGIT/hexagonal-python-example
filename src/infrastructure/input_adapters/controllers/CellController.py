from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.cell.ports.CellGateway import CellGateway
from src.domain.entities.cell.value_objects.CellId import CellId
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.CellDTO import CellDTO
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class CellController:

    __cellGateway: CellGateway

    def __init__(self, useCase: CellGateway):
        self.__cellGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/create-cell")
        async def createReservation(request: CellDTO):
            try:
                self.__cellGateway.createCell(
                    request.spaceNumber,
                    request.vehicleType,
                    request.status
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_CREATED_USER)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )

        @app.put("/update-cell/{cell_id}")
        async def updateEmployee(cell_id: str, request: CellDTO):
            try:
                cellId = CellId(cell_id)
                self.__cellGateway.updateCell(
                    cellId=cellId,
                    vehicleType=request.vehicleType,
                    status=request.status,
                    spaceNumber=request.spaceNumber
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_UPDATED_CELL)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )
