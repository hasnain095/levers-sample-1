from typing import TYPE_CHECKING, Optional, List

from sqlalchemy import String, Float
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, ForeignKey

from app.db.base_class import Base


class SubBill(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    reference: Mapped[Optional[str]] = mapped_column(String(255))
    bill_id: Mapped[int] = mapped_column(ForeignKey("bill.id"))
    bill: Mapped["Bill"] = relationship(back_populates="subbills")


    __table_args__ = (
        UniqueConstraint("reference"),
    )


