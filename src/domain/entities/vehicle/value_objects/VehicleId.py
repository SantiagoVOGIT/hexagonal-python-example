import uuid


class VehicleId:

    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def generate() -> 'VehicleId':
        return VehicleId(str(uuid.uuid4()))
