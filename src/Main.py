from fastapi import FastAPI
import logging

from src.application.use_cases.AuthUseCase import AuthUseCase
from src.application.use_cases.CellUseCase import CellUseCase
from src.application.use_cases.EmployeeUseCase import EmployeeUseCase
from src.application.use_cases.ReservationUseCase import ReservationUseCase
from src.application.use_cases.VehicleUseCase import VehicleUseCase
from src.infrastructure.common.DatabaseService import DatabaseService
from src.infrastructure.config.CorsConfig import CorsConfig

from src.infrastructure.input_adapters.controllers.AuthController import AuthController
from src.infrastructure.input_adapters.controllers.CellController import CellController
from src.infrastructure.input_adapters.controllers.EmployeeController import EmployeeController
from src.infrastructure.input_adapters.controllers.HealthController import HealthController
from src.infrastructure.input_adapters.controllers.ReservationController import ReservationController
from src.infrastructure.input_adapters.controllers.VehicleController import VehicleController
from src.infrastructure.output_adapters.persistence.repositories.CellPostgreRepository import CellPostgreRepository
from src.infrastructure.output_adapters.persistence.repositories.EmployeePostgreRepository import EmployeePostgreRepository
from src.infrastructure.output_adapters.persistence.repositories.ReservationPostgreRepository import ReservationPostgreRepository
from src.infrastructure.output_adapters.persistence.repositories.UserPostgreRepository import UserPostgreRepository
from src.infrastructure.output_adapters.persistence.repositories.VehiclePostgreRepository import VehiclePostgreRepository


class Main:

    __app: FastAPI
    __databaseService: DatabaseService

    __healthController: HealthController
    __authController: AuthController
    __cellController: CellController
    __vehicleController: VehicleController
    __reservationController: ReservationController
    __employeeController: EmployeeController

    def __init__(self):
        self.__app = FastAPI()
        self.__databaseService = DatabaseService()
        self.__healthController = HealthController()
        self.__authController = self.__configAuthController()
        self.__cellController = self.__configCellController()
        self.__vehicleController = self.__configVehicleController()
        self.__reservationController = self.__configReservationController()
        self.__employeeController = self.__configEmployeeController()

    def __configAuthController(self) -> AuthController:
        outputAdapter = UserPostgreRepository(self.__databaseService)
        useCase = AuthUseCase(outputAdapter)
        inputAdapter = AuthController(useCase)
        return inputAdapter

    def __configCellController(self) -> CellController:
        outputAdapter = CellPostgreRepository(self.__databaseService)
        useCase = CellUseCase(outputAdapter)
        inputAdapter = CellController(useCase)
        return inputAdapter

    def __configVehicleController(self) -> VehicleController:
        outputAdapter = VehiclePostgreRepository(self.__databaseService)
        useCase = VehicleUseCase(outputAdapter)
        inputAdapter = VehicleController(useCase)
        return inputAdapter

    def __configReservationController(self) -> ReservationController:
        reservationOutputAdapter = ReservationPostgreRepository(self.__databaseService)
        cellOutputAdapter = CellPostgreRepository(self.__databaseService)
        vehicleOutputAdapter = VehiclePostgreRepository(self.__databaseService)
        useCase = ReservationUseCase(reservationOutputAdapter, cellOutputAdapter, vehicleOutputAdapter)
        inputAdapter = ReservationController(useCase)
        return inputAdapter

    def __configEmployeeController(self) -> EmployeeController:
        outputAdapter = EmployeePostgreRepository(self.__databaseService)
        outputAdapterHelper = UserPostgreRepository(self.__databaseService)
        useCase = EmployeeUseCase(outputAdapter, outputAdapterHelper)
        inputAdapter = EmployeeController(useCase)
        return inputAdapter

    def setupControllers(self) -> None:
        self.__healthController.setupRoutes(self.__app)
        self.__authController.setupRoutes(self.__app)
        self.__cellController.setupRoutes(self.__app)
        self.__vehicleController.setupRoutes(self.__app)
        self.__reservationController.setupRoutes(self.__app)
        self.__employeeController.setupRoutes(self.__app)

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
