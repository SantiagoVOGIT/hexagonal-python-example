import uuid


class VehicleTypeId:

    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def generate() -> 'VehicleTypeId':
        return VehicleTypeId(str(uuid.uuid4()))
