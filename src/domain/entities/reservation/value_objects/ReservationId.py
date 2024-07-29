import uuid

from src.domain.common.EntityId import EntityId


class ReservationId(EntityId):

    def __init__(self, value: str):
        super().__init__(value)
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @classmethod
    def generate(cls) -> 'ReservationId':
        return cls(str(uuid.uuid4()))
