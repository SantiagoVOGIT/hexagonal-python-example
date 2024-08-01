from typing import Dict, Any

from fastapi import FastAPI, HTTPException

from src.domain.entities.user.ports.AuthGateway import AuthGateway
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo
from src.infrastructure.input_adapters.dto.UserDTO import UserDTO
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.utils.MessageFactory import MessageFactory


class AuthController:

    __authGateway: AuthGateway

    def __init__(self, useCase: AuthGateway):
        self.__authGateway = useCase

    def setupRoutes(self, app: FastAPI) -> None:

        @app.post("/login")
        async def login(request: UserDTO):
            try:
                self.__authGateway.login(
                    request.emailAddress,
                    request.dniNumber
                )
                return {
                    "detail": MessageFactory
                    .build(InfrastructureInfo.SUCCES_LOGIN)
                    .getDetail()
                }
            except Exception as exc:
                errorResponse: Dict[str, Any] = ExceptionHandler.handleException(exc)
                raise HTTPException(
                    status_code=400, detail=errorResponse
                )
