from src.domain.entities.cell.CellFactory import CellFactory
from src.domain.entities.cell.value_objects.CellStatus import CellStatus
from src.domain.entities.cell.value_objects.SpaceNumber import SpaceNumber
from src.domain.entities.reservation.ReservationFactory import ReservationFactory
from src.domain.entities.user.UserFactory import UserFactory
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.vehicle.VehicleFactory import VehicleFactory
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType

dni_type = DniType.TI
user_role = UserRole.USER
cellNumber = SpaceNumber.CELDA_UNO

user1 = UserFactory.create(
    dniNumber="1036928592",
    dniType=dni_type,
    firstName="Santiago",
    lastName="Valencia",
    role=user_role,
    phoneNumber="3024508215",
    emailAddress="fenixcaps@gmail.com"
)

cell1 = CellFactory.create(
    spaceNumber=cellNumber,
    vehicleType=VehicleType.CAR,
    status=CellStatus.OCCUPIED,
)

vehicle1 = VehicleFactory.create(
    userId=user1.getId(),
    licensePlate="AAA777",
    model="Ferrari a243",
    vehicleType=VehicleType.CAR
)

reservation1 = ReservationFactory.create(
    userId=user1.getId(),
    cellId=cell1.getId(),
    vehicleId=vehicle1.getId(),
)

print(user1.getId().getValue())
print(reservation1.getUserId().getValue())
print(cell1.getStatus().getValue())
