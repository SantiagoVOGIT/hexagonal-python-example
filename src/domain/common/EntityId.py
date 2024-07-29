import uuid


class EntityId:

    def __init__(self, value: str = None):
        self.__value = value if value else str(uuid.uuid4())

    def getValue(self) -> str:
        return self.__value

    def __str__(self):
        return self.__value

    def __eq__(self, other):
        if isinstance(other, EntityId):
            return self.__value == other.__value
        return False

    def __hash__(self):
        return hash(self.__value)
