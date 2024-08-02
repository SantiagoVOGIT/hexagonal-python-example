from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.user.ports.UserGateway import UserGateway
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.UserDTO import UserDTO
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class UserController:

    __userGateway: UserGateway

    def __init__(self, useCase: UserGateway):
        self.__userGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/register")
        async def register(request: UserDTO):
            try:
                self.__userGateway.createUser(
                    dniNumber=request.dniNumber,
                    firstName=request.firstName,
                    lastName=request.lastName,
                    dniType=request.dniType,
                    emailAddress=request.emailAddress,
                    phoneNumber=request.phoneNumber,
                    status=UserStatus.ACTIVE,
                    role=UserRole.USER
                )
                return {
                    "message": MessageFactory
                    .build(InfrastructureInfo.SUCCES_REGISTERED_USER)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(status_code=400, detail=errorResponse)

        @app.post("/admin/create-user")
        async def createReservation(request: UserDTO):
            try:
                self.__userGateway.createUser(
                    dniNumber=request.dniNumber,
                    firstName=request.firstName,
                    lastName=request.lastName,
                    dniType=request.dniType,
                    emailAddress=request.emailAddress,
                    phoneNumber=request.phoneNumber,
                    status=request.status,
                    role=request.role,
                )
                return {
                    "message": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_CREATED_USER)
                    .getDetail()
                }

            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(status_code=400, detail=errorResponse)

        @app.put("/admin/update-user/{user_id}")
        async def updateUser(user_id: str, request: UserDTO):
            try:
                userId = UserId(user_id)
                self.__userGateway.updateUser(
                    userId=userId,
                    dniNumber=request.dniNumber,
                    dniType=request.dniType,
                    firstName=request.firstName,
                    lastName=request.lastName,
                    emailAddress=request.emailAddress,
                    phoneNumber=request.phoneNumber,
                    role=request.role,
                    status=request.status
                )
                return {
                    "message": MessageFactory
                    .build(InfrastructureInfo.SUCCESS_UPDATED_USER)
                    .getDetail()
                }

            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(status_code=400, detail=errorResponse)

        @app.put("/update-user/{user_id}")
        async def updateUser(user_id: str, request: UserDTO):
            try:
                userId = UserId(user_id)
                self.__userGateway.updateUser(
                    userId=userId,
                    dniType=request.dniType,
                    firstName=request.firstName,
                    lastName=request.lastName,
                    emailAddress=request.emailAddress,
                    phoneNumber=request.phoneNumber,
                )
                return {
                    "message": MessageFactory
                    .build(InfrastructureInfo.SUCCES_UPDATED_USER_BASIC_INFO)
                    .getDetail()
                }

            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(status_code=400, detail=errorResponse)
