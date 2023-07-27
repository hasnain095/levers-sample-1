from typing import TYPE_CHECKING, Optional, List

from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

from app.db.base_class import Base


class Bill(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    total: Mapped[float] = mapped_column(Float, nullable=False)
    subbills: Mapped[List["SubBill"]] = relationship(back_populates="bill")
