from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID

class EntityIdAdapter(TypeDecorator):

    impl = CHAR
    cache_ok = True  # Añade esta línea

    def __init__(self, id_class):
        self.impl = UUID(as_uuid=True)
        self.id_class = id_class
        super().__init__(36)

    def processBindParam(self, value, dialect):
        if value is None:
            return value
        elif isinstance(value, str):
            return value
        elif isinstance(value, self.id_class):
            return value.getValue()
        else:
            raise ValueError(f"Invalid {self.id_class.__name__} value")

    def processResultValue(self, value, dialect):
        if value is None:
            return value
        else:
            return self.id_class(str(value))