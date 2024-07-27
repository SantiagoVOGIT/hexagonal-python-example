from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.domain.entities.user.value_objects.UserId import UserId
from src.infrastructure.output_adapters.persistence.entities.vehicle_data.VehicleData import VehicleData


class VehicleMapper:

    @staticmethod
    def toDomain(vehicleData: VehicleData) -> Vehicle:
        return Vehicle(
            id=VehicleId(vehicleData.id),
            userId=UserId(vehicleData.user_id),
            licensePlate=vehicleData.license_plate,
            model=vehicleData.model,
            vehicleType=VehicleType(vehicleData.vehicle_type),
            registeredAt=vehicleData.created_at
        )

    @staticmethod
    def toPersistence(vehicle: Vehicle) -> VehicleData:
        return VehicleData(
            id=vehicle.getId().getValue(),
            user_id=vehicle.getUserId().getValue(),
            license_plate=vehicle.getLicensePlate(),
            model=vehicle.getModel(),
            vehicle_type=vehicle.getVehicleType().getValue(),
            created_at=vehicle.getRegisteredAt()
        )
