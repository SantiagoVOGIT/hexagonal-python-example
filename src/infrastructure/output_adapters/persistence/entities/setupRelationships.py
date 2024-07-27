from sqlalchemy.orm import relationship

def setupRelationships():

    from src.infrastructure.output_adapters.persistence.entities.user_data.UserData import UserData
    from src.infrastructure.output_adapters.persistence.entities.vehicle_data.VehicleData import VehicleData
    from src.infrastructure.output_adapters.persistence.entities.cell_data.CellData import CellData
    from src.infrastructure.output_adapters.persistence.entities.employee_data.EmployeeData import EmployeeData
    from src.infrastructure.output_adapters.persistence.entities.reservation_data.ReservationData import ReservationData

    # UserData relationships
    UserData.vehicles = relationship("VehicleData", back_populates="user")
    UserData.reservations = relationship("ReservationData", back_populates="user")
    UserData.employee = relationship("EmployeeData", back_populates="user", uselist=False)

    # VehicleData relationships
    VehicleData.user = relationship("UserData", back_populates="vehicles")
    VehicleData.reservations = relationship("ReservationData", back_populates="vehicle")

    # CellData relationships
    CellData.reservations = relationship("ReservationData", back_populates="cell")

    # EmployeeData relationships
    EmployeeData.user = relationship("UserData", back_populates="employee")

    # ReservationData relationships
    ReservationData.user = relationship("UserData", back_populates="reservations")
    ReservationData.vehicle = relationship("VehicleData", back_populates="reservations")
    ReservationData.cell = relationship("CellData", back_populates="reservations")