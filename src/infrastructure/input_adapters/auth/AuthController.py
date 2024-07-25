from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.user.ports.UserGateway import UserGateway
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus
from src.domain.input_ports.AuthGateway import AuthGateway
from src.shared.utils.ErrorHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory
from src.domain.entities.user.User import User
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.auth.LoginDTO import LoginDTO
from src.infrastructure.input_adapters.auth.RegisterDTO import RegisterDTO

from pydantic import BaseModel

from src.domain.entities.user.value_objects.DniType import DniType


class UserDTO(BaseModel):
    dniNumber: str
    dniType: DniType
    firstName: str
    lastName: str
    phoneNumber: str
    emailAddress: str
    rol: UserRole
    status: UserStatus

class AuthController:

    __authGateway: AuthGateway
    __userGateway: UserGateway

    def __init__(self, authuseCase: AuthGateway, userUseCase: UserGateway):
        self.__authGateway = authuseCase
        self.__userGateway = userUseCase

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
