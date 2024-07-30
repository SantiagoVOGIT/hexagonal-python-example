from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.employee.ports.EmployeeGateway import EmployeeGateway
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.EmployeeDTO import EmployeeDTO
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class EmployeeController:

    employeeGateway: EmployeeGateway

    def __init__(self, useCase: EmployeeGateway):
        self.employeeGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/create-employee")
        async def createEmployee(request: EmployeeDTO):
            try:
                self.employeeGateway.createEmployee(
                    request.userId,
                    request.position,
                    request.salary
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCES_CREATED_EMPLOYEE)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400,
                    detail=errorResponse
                )
