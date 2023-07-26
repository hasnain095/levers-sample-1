from typing import TYPE_CHECKING

>>> from sqlalchemy import String
>>> from sqlalchemy.orm import DeclarativeBase
>>> from sqlalchemy.orm import Mapped
>>> from sqlalchemy.orm import mapped_column
>>> from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

from app.db.base_class import Base


class SubBill(Base):
 	id: Mapped[int] = mapped_column(primary_key=True)
    amount = Column(Float)
    name: Mapped[Optional[str] = mapped_column(String(255))

    __table_args__ = (
        UniqueConstraint("name"),
    )


