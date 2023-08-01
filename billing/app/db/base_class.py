from typing import Any

from sqlalchemy.orm import registry
from sqlalchemy.orm import declared_attr
from sqlalchemy import Column, Integer

mapper_registry = registry()


@mapper_registry.as_declarative_base()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = Column(Integer, primary_key=True)
