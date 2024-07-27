from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.user.User import User
from src.domain.input_ports.AuthGateway import AuthGateway
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.UserDTO import UserDTO
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class AuthController:

    __authGateway: AuthGateway

    def __init__(self, useCase: AuthGateway):
        self.__authGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/register")
        async def register(request: UserDTO):
            try:
                newUser: User = self.__authGateway.register(
                    request.dniNumber,
                    request.dniType,
                    request.firstName,
                    request.lastName,
                    request.phoneNumber,
                    request.emailAddress
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCES_REGISTERED_USER)
                    .getDetail(),
                    "user": f"{newUser.getFirstName()}, {newUser.getLastName()}"
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400, detail=errorResponse
                )

        @app.post("/login")
        async def login(request: UserDTO):
            try:
                user: User = self.__authGateway.login(
                    request.emailAddress,
                    request.dniNumber
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCES_LOGIN)
                    .getDetail(),
                    "user": f"{user.getFirstName()}, {user.getLastName()}"
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400, detail=errorResponse
                )
