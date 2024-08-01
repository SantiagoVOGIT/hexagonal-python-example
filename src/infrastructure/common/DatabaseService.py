import logging
import os
from typing import Optional, Type

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session, DeclarativeMeta, declarative_base, DeclarativeBase

from src.infrastructure.output_adapters.common.setupRelationships import setupRelationships
from src.shared.error.CustomException import CustomException
from src.shared.error.ExceptionHandler import ExceptionHandler
from src.shared.error.enums.ErrorType import ErrorType
from src.shared.utils.MessageFactory import MessageFactory
from src.shared.error.enums.InfrastructureErrorType import InfrastructureErrorType
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo


class DatabaseService:

    __DATABASE_URL: str = os.getenv("DATABASE_URL")
    __engine: Engine
    __sessionMaker: sessionmaker = None
    __session: Optional[Session] = None
    __base: DeclarativeMeta = declarative_base()

    def __init__(self) -> None:
        self.__engine = self.__createEngine()
        self.__sessionMaker = self.__createSessionMaker()
        self.__setupRelationships()

    def __createEngine(self) -> Engine:
        if not self.__DATABASE_URL:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.ENV_DB_NOT_SET.name,
                InfrastructureErrorType.ENV_DB_NOT_SET.value
            ))
        return create_engine(self.__DATABASE_URL)

    def __createSessionMaker(self) -> sessionmaker:
        return sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.__engine
        )

    def getSession(self) -> Session:
        if self.__session is None:
            self.__session = self.__sessionMaker()
        return self.__session

    @classmethod
    def getBase(cls) -> Type[DeclarativeBase]:
        return cls.__base

    @staticmethod
    def __setupRelationships():
        setupRelationships()

    def checkConnection(self) -> bool:
        try:
            with self.getSession() as session:
                session.execute(text("SELECT 1"))
            logging.info(
                MessageFactory
                .build(InfrastructureInfo.SUCCESS_CONNECTION_DATABASE)
                .getDetail()
            )
            return True
        except SQLAlchemyError as exc:
            ExceptionHandler.raiseException(CustomException(
                ErrorType.INFRASTRUCTURE_ERROR,
                InfrastructureErrorType.ERROR_CONNECTION_DB.name,
                InfrastructureErrorType.ERROR_CONNECTION_DB.value,
                {"original_error": str(exc)}
            ))
        finally:
            if session:
                session.close()
