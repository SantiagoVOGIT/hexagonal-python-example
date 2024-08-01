from typing import Optional, Dict, Any

from src.shared.error.CustomException import CustomException
from src.shared.error.enums.DomainErrorType import DomainErrorType
from src.shared.error.enums.ErrorType import ErrorType


class DomainException(CustomException):

    def __init__(self, domainErrorType: DomainErrorType, additionalInfo: Optional[Dict[str, Any]] = None):
        super().__init__(
            ErrorType.DOMAIN_ERROR,
            domainErrorType.name,
            domainErrorType.value,
            additionalInfo
        )
