from datetime import datetime

from src.domain.entities.employee.value_objects.EmployeeId import EmployeeId
from src.domain.entities.employee.value_objects.EmployeePosition import EmployeePosition
from src.domain.entities.user.value_objects.UserId import UserId


class Employee:

    __id: EmployeeId
    __userId: UserId
    __position: EmployeePosition
    __hireDate: datetime
    __salary: float
    __createdAt: datetime

    def __init__(self,
                 id: EmployeeId,
                 userId: UserId,
                 position: EmployeePosition,
                 hireDate: datetime,
                 salary: float,
                 createdAt: datetime):
        self.__id = id
        self.__userId = userId
        self.__position = position
        self.__hireDate = hireDate
        self.__salary = salary
        self.__createdAt = createdAt

    def getId(self) -> EmployeeId:
        return self.__id

    def getUserId(self) -> UserId:
        return self.__userId

    def getPosition(self) -> EmployeePosition:
        return self.__position

    def getHireDate(self) -> datetime:
        return self.__hireDate

    def getSalary(self) -> float:
        return self.__salary

    def getCreatedAt(self) -> datetime:
        return self.__createdAt
