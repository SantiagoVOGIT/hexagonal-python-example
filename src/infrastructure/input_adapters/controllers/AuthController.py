from fastapi import FastAPI
from pydantic import BaseModel

from src.application.input_ports.AuthGateway import AuthGateway
from src.common.utils.MessageFactory import MessageFactory
from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from fastapi import HTTPException


class RegisterRequest(BaseModel):
    dniNumber: str
    dniType: DniType
    firstName: str
    lastName: str
    phoneNumber: str
    emailAddress: str


class LoginRequest(BaseModel):
    emailAddress: str
    dniNumber: str


class AuthController:
    __authInputPort: AuthGateway

    def __init__(self, inputPort: AuthGateway):
        self.__authInputPort = inputPort

    def setupRoutes(self, app: FastAPI) -> None:
        @app.post("/register")
        async def register(request: RegisterRequest):
            try:
                user: User = self.__authInputPort.register(
                    request.dniNumber,
                    request.dniType,
                    request.firstName,
                    request.lastName,
                    request.phoneNumber,
                    request.emailAddress
                )
                return {
                    "detail":
                        MessageFactory
                        .build(InfrastructureInfo.SUCCES_REGISTERED_USER)
                        .getDetail(),
                    "user":
                        user.getFirstName()
                }

            except ValueError as exc:
                raise HTTPException(
                    status_code=400, detail=str(exc)
                )

        @app.post("/login")
        async def login(request: LoginRequest):
            try:
                user: User = self.__authInputPort.login(
                    request.emailAddress,
                    request.dniNumber
                )
                return {
                    "detail":
                        MessageFactory
                        .build(InfrastructureInfo.SUCCES_LOGIN)
                        .getDetail(),
                    "user":
                        user.getFirstName()
                }

            except ValueError as exc:
                raise HTTPException(
                    status_code=400, detail=str(exc)
                )
