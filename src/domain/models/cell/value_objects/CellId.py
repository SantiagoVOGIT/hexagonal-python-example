import uuid


class CellId:

    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def generate() -> 'CellId':
        return CellId(str(uuid.uuid4()))
