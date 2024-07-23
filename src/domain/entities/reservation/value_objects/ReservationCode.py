import uuid


class ReservationCode:

    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def __generateCode() -> str:
        return uuid.uuid4().hex[:10].upper()

    @staticmethod
    def generate() -> 'ReservationCode':
        return ReservationCode(ReservationCode.__generateCode())
