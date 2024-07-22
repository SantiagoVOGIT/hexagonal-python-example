from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.infrastructure.config.Environments import Environments


class CorsConfig:

    __ALLOWED_ORIGINS: List[str] = [
        Environments.getCurrentUrlFr(),
    ]
    __ALLOW_CREDENTIALS: bool = True
    __ALLOW_METHODS: List[str] = ["*"]
    __ALLOW_HEADERS: List[str] = ["*"]

    @staticmethod
    def setup(app: FastAPI) -> None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=CorsConfig.__ALLOWED_ORIGINS,
            allow_credentials=CorsConfig.__ALLOW_CREDENTIALS,
            allow_methods=CorsConfig.__ALLOW_METHODS,
            allow_headers=CorsConfig.__ALLOW_HEADERS,
        )

    @staticmethod
    def getAllowedOrigins() -> List[str]:
        return CorsConfig.__ALLOWED_ORIGINS
