from src.domain.entities.vehicle.Vehicle import Vehicle
from src.domain.entities.vehicle.value_objects.VehicleId import VehicleId
from src.domain.entities.vehicle.value_objects.VehicleType import VehicleType
from src.domain.entities.user.value_objects.UserId import UserId
from src.infrastructure.output_adapters.persistence.entities.vehicle_data.VehicleModel import VehicleModel


class VehicleMapper:

    @staticmethod
    def toDomain(vehicleModel: VehicleModel) -> Vehicle:
        return Vehicle(
            id=VehicleId(vehicleModel.id),
            userId=UserId(vehicleModel.user_id),
            licensePlate=vehicleModel.license_plate,
            model=vehicleModel.model,
            vehicleType=VehicleType(vehicleModel.vehicle_type),
            registeredAt=vehicleModel.created_at
        )

    @staticmethod
    def toPersistence(vehicle: Vehicle) -> VehicleModel:
        return VehicleModel(
            id=vehicle.getId().getValue(),
            user_id=vehicle.getUserId().getValue(),
            license_plate=vehicle.getLicensePlate(),
            model=vehicle.getModel(),
            vehicle_type=vehicle.getVehicleType().getValue(),
            created_at=vehicle.getRegisteredAt()
        )