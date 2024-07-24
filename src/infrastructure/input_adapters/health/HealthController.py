from typing import Dict
from fastapi import FastAPI

from src.common.utils.MessageFactory import MessageFactory
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo


class HealthController:

    @staticmethod
    def setupRoutes(app: FastAPI) -> None:

        @app.get("/")
        async def apiStatus() -> Dict[str, str]:
            return {
                "message": MessageFactory
                .build(InfrastructureInfo.CURRENT_ENVIRONMENT_API)
                .getDetail()
            }
