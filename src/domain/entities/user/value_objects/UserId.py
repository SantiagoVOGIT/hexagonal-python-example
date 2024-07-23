import uuid


class UserId:

    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def generate() -> 'UserId':
        return UserId(str(uuid.uuid4()))
