import uuid


class ReservationId:

    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def generate() -> 'ReservationId':
        return ReservationId(str(uuid.uuid4()))
