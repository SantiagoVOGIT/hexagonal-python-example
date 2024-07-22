from fastapi import FastAPI
import logging

from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.config.CorsConfig import CorsConfig
from src.infrastructure.input_adapters.controllers.HealthController import HealthController


class Main:
    __app: FastAPI
    __dbService: DatabaseService
    __healthController: HealthController

    def __init__(self):
        self.__app = FastAPI()
        self.__dbService = DatabaseService()
        self.__healthController = HealthController()

    def setupControllers(self) -> None:
        self.__healthController.setupRoutes(self.__app)

    def ensureConnection(self) -> None:
        self.__dbService.checkConnection()

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
