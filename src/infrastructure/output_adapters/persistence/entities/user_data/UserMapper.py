from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus
from src.infrastructure.output_adapters.persistence.entities.user_data.UserModel import UserModel


class UserMapper:

    @staticmethod
    def toDomain(userModel: UserModel) -> User:
        return User(
            id=UserId(userModel.id),
            dniNumber=userModel.dni_number,
            dniType=DniType(userModel.dni_type),
            firstName=userModel.first_name,
            lastName=userModel.last_name,
            emailAddress=userModel.email_address,
            role=UserRole(userModel.role),
            status=UserStatus(userModel.status),
            phoneNumber=userModel.phone_number,
            createdAt=userModel.created_at
        )

    @staticmethod
    def toPersistence(user: User) -> UserModel:
        return UserModel(
            id=user.getId().getValue(),
            dni_number=user.getDniNumber(),
            dni_type=user.getDniType().getValue(),
            first_name=user.getFirstName(),
            last_name=user.getLastName(),
            email_address=user.getEmailAddress(),
            role=user.getRole().getValue(),
            status=user.getStatus().getValue(),
            phone_number=user.getPhoneNumber(),
            created_at=user.getCreatedAt()
        )
