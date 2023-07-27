from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.subbill import SubBill
from app.schemas.subbill import SubBillCreate, SubBillUpdate
from sqlalchemy import select, insert, literal_column


class CRUDSubBill(CRUDBase[SubBill, SubBillCreate, SubBillUpdate]):
    def create_with_bill(
        self, db: Session, *, obj_in: SubBillCreate, bill_id: int
    ) -> SubBill:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, bill_id=bill_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def exists(
        self, db: Session, *, obj_in: List[SubBillCreate]
        ) -> List[SubBill]:
        references = [x.reference for x in obj_in]
        stmt = select(self.model).where(self.model.reference.in_(references))
        result = db.execute(stmt)
        return result.scalars().all()


    # def get_multi_by_owner(
    #     self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    # ) -> List[Item]:
    #     return (
    #         db.query(self.model)
    #         .filter(Item.owner_id == owner_id)
    #         .offset(skip)
    #         .limit(limit)
    #         .all()
    #     )


subbill = CRUDSubBill(SubBill)
