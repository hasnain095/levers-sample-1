from typing import List, Type, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.bill import Bill
from app.models.subbill import SubBill as SubBillModel
from app.schemas.bill import BillCreate, BillUpdate, BillBase
from app.schemas.subbill import SubBill, SubBillCreate
from sqlalchemy import select, insert, literal_column, distinct



class CRUDBill(CRUDBase[Bill, BillCreate, BillUpdate]):
    def create_bill_with_subbill(
        self, db: Session, *, obj_in: BillCreate
    ) -> Bill:
        bill_to_create = BillBase(total=obj_in.total)
        bill_json = jsonable_encoder(bill_to_create)
        bill_stmt = insert(self.model).values(bill_json).returning(self.model)
        result = db.execute(bill_stmt)
        bill_created = result.scalars().first()
        bill_id = bill_created.id

        subbills = obj_in.subbills
        subbills_to_create = [SubBillCreate(amount=x.amount, reference=x.reference, bill_id=bill_id) for x in subbills]
        subbills_to_create_json = jsonable_encoder(subbills_to_create)
        subbill_stmt = insert(SubBillModel).values(subbills_to_create_json).returning(SubBillModel)
        result = db.execute(subbill_stmt)
        
        db.commit()

        stmt = select(self.model).where(self.model.id==bill_id)
        result = db.execute(stmt)
        return result.scalars().first()

    def filter(self,db: Session, reference: Optional[str], total_from: Optional[float], total_to: Optional[float]):

        stmt = select(self.model)

        if reference:
            stmt = stmt.join(self.model.subbills.and_(SubBillModel.reference.icontains(reference)))
        elif total_from:
            stmt = stmt.where(self.model.total >= total_from)
        elif total_to:
            stmt = stmt.where(self.model.total <= total_to)

        print(stmt)

        result = db.execute(stmt.distinct())
        return result.scalars().all()


bill = CRUDBill(Bill)
