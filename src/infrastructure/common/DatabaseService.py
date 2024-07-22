import logging
import os
from typing import Optional, Type

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker, DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base

from src.common.utils.ExceptionFactory import ExceptionFactory
from src.common.utils.MessageFactory import MessageFactory
from src.infrastructure.common.enums.InfrastructureError import InfrastructureError
from src.infrastructure.common.enums.InfrastructureInfo import InfrastructureInfo


class DatabaseService:

    base: Type[DeclarativeMeta] = declarative_base()
    __DATABASE_URL: str = os.getenv("DATABASE_URL")
    __engine: Engine
    __sessionMaker: sessionmaker = None
    __session: Optional[Session] = None

    def __init__(self) -> None:
        self.__engine = self.__createEngine()
        self.__sessionMaker = self.__createSessionMaker()

    def __createEngine(self) -> Engine:
        if not self.__DATABASE_URL:
            raise ValueError(
                ExceptionFactory
                .build(InfrastructureError.ENV_DB_NOT_SET)
                .getDetail()
            )
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

    def createAllTables(self):
        self.base.metadata.create_all(self.__engine)

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
            logging.error(
                ExceptionFactory
                .build(InfrastructureError.ERROR_CONNECTION_DB)
                .getDetail(exc)
            )
            return False
        finally:
            if session:
                session.close()
