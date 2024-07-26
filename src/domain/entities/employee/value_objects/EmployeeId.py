import uuid


class EmployeeId:

    __value: str

    def __init__(self, value: str):
        self.__value = value

    def getValue(self) -> str:
        return self.__value

    @staticmethod
    def generate() -> 'EmployeeId':
        return EmployeeId(str(uuid.uuid4()))
