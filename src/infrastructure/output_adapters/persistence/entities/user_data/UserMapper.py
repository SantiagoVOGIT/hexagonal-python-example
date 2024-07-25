from src.domain.entities.user.User import User
from src.domain.entities.user.value_objects.DniType import DniType
from src.domain.entities.user.value_objects.UserId import UserId
from src.domain.entities.user.value_objects.UserRole import UserRole
from src.domain.entities.user.value_objects.UserStatus import UserStatus
from src.infrastructure.output_adapters.persistence.entities.user_data.UserData import UserData


class UserMapper:

    @staticmethod
    def toDomain(userData: UserData) -> User:
        return User(
            id=UserId(userData.id),
            dniNumber=userData.dni_number,
            dniType=DniType(userData.dni_type),
            firstName=userData.first_name,
            lastName=userData.last_name,
            emailAddress=userData.email_address,
            role=UserRole(userData.role),
            status=UserStatus(userData.status),
            phoneNumber=userData.phone_number,
            createdAt=userData.created_at
        )

    @staticmethod
    def toPersistence(user: User) -> UserData:
        return UserData(
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
