from typing import Optional

from pydantic import BaseModel


class SubBillBase(BaseModel):
	amount: float
	reference: Optional[str]


class SubBillCreate(SubBillBase):
	bill_id: int


class SubBillUpdate(SubBillCreate):
	pass


class SubBill(BaseModel):
	pass

