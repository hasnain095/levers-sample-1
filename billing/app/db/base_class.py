from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


from sqlalchemy.orm import registry

mapper_registry = registry()

@mapper_registry.as_declarative_base()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()