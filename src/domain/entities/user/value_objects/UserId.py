import uuid

from src.domain.common.EntityId import EntityId


class UserId(EntityId):

    def __init__(self, value: str):
        super().__init__(value)
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @classmethod
    def generate(cls) -> 'UserId':
        return cls(str(uuid.uuid4()))
