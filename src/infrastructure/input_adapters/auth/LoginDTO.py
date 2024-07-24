from pydantic import BaseModel


class LoginDTO(BaseModel):
    emailAddress: str
    dniNumber: str