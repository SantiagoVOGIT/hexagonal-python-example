from fastapi import FastAPI
import logging

from src.application.use_cases.AuthUseCase import AuthUseCase
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.config.CorsConfig import CorsConfig
from src.infrastructure.input_adapters.controllers.AuthController import AuthController
from src.infrastructure.input_adapters.controllers.HealthController import HealthController
from src.infrastructure.output_adapters.persistence.repositories.PostgreSQLRepository import PostgreSQLRepository


class Main:

    __app: FastAPI
    __databaseService: DatabaseService
    __healthController: HealthController
    __authController: AuthController

    def __init__(self):
        self.__app = FastAPI()
        self.__databaseService = DatabaseService()
        self.__healthController = HealthController()
        self.__authController = self.__configAuthController()

    def __configAuthController(self) -> AuthController:
        repository = PostgreSQLRepository(self.__databaseService)
        authUseCase = AuthUseCase(repository)
        return AuthController(authUseCase)

    def setupControllers(self) -> None:
        self.__healthController.setupRoutes(self.__app)
        self.__authController.setupRoutes(self.__app)

    def ensureConnection(self) -> None:
        self.__databaseService.checkConnection()

    def setupConfig(self) -> None:
        logging.basicConfig(level=logging.INFO)
        CorsConfig.setup(self.__app)

    def getApp(self) -> FastAPI:
        return self.__app

    @staticmethod
    def initialize() -> FastAPI:
        main = Main()
        main.setupConfig()
        main.setupControllers()
        main.ensureConnection()
        return main.getApp()


app: FastAPI = Main.initialize()
