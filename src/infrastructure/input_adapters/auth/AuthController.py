from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.application.input_ports.AuthGateway import AuthGateway
from src.common.utils.ErrorHandler import ExceptionHandler
from src.common.utils.MessageFactory import MessageFactory
from src.domain.entities.user.User import User
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.auth.LoginDTO import LoginDTO
from src.infrastructure.input_adapters.auth.RegisterDTO import RegisterDTO


class AuthController:

    __authGateway: AuthGateway

    def __init__(self, inputPort: AuthGateway):
        self.__authGateway = inputPort

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/register")
        async def register(request: RegisterDTO):
            try:
                user: User = self.__authGateway.register(
                    request.dniNumber,
                    request.dniType,
                    request.firstName,
                    request.lastName,
                    request.phoneNumber,
                    request.emailAddress
                )
                return {
                    "detail": MessageFactory.build(InfrastructureInfo.SUCCES_REGISTERED_USER).getDetail(),
                    "user": user.getFirstName()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400, detail=errorResponse
                )

        @app.post("/login")
        async def login(request: LoginDTO):
            try:
                user: User = self.__authGateway.login(
                    request.emailAddress,
                    request.dniNumber
                )
                return {
                    "detail": MessageFactory.build(InfrastructureInfo.SUCCES_LOGIN).getDetail(),
                    "user": user.getFirstName()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400, detail=errorResponse
                )
