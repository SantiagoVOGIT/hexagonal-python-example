from typing import Dict, Any, List

from fastapi import FastAPI, HTTPException

from src.domain.entities.employee.Employee import Employee
from src.domain.entities.employee.ports.EmployeeGateway import EmployeeGateway
from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.EmployeeDTO import EmployeeDTO
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class EmployeeController:

    __employeeGateway: EmployeeGateway

    def __init__(self, useCase: EmployeeGateway):
        self.__employeeGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/admin/create-employee")
        async def createEmployee(request: EmployeeDTO):
            try:
                self.__employeeGateway.createEmployee(
                    request.userId,
                    request.position,
                    request.status,
                    request.salary
                )
                return {
                    "message": MessageFactory
                    .build(InfrastructureInfo.SUCCES_CREATED_EMPLOYEE)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(status_code=400, detail=errorResponse)

        @app.put("/admin/update-employee/{employee_id}")
        async def updateEmployee(employee_id: str, request: EmployeeDTO):
            try:
                employeeId = EmployeeId(employee_id)
                self.__employeeGateway.updateEmployee(
                    employeeId=employeeId,
                    userId=request.userId,
                    position=request.position,
                    status=request.status,
                    salary=request.salary
                )
                return {
                    "message": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_UPDATED_EMPLOYEE)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(status_code=400, detail=errorResponse)

        @app.get("/admin/employees")
        async def getAllEmployees():
            try:
                employees: List[Employee] = self.__employeeGateway.getAllEmployees()
                return {
                    "employees": [
                        Employee.toDict(employee)
                        for employee
                        in employees
                    ]
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(status_code=400, detail=errorResponse)
