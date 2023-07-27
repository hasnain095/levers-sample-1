from typing import Optional, List

from pydantic import BaseModel

from .subbill import SubBillBase


class BillBase(BaseModel):
	total: float 


class BillCreate(BillBase):
	subbills: List[SubBillBase]


class BillUpdate(BillBase):
	pass


class BillInDB(BillBase):
	id: int


class Bill(BillInDB):
	pass

	class Config:
		orm_mode = True

class BillRead(BillInDB):
	id: int
	subbills: List[SubBillBase]
	
	class Config:
		orm_mode = True

class BillQuery(BaseModel):
	reference: Optional[str]
	total_from: Optional[float]
	total_to: Optional[float]