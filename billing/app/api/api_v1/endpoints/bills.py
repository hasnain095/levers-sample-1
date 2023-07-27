from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/bills", response_model=List[schemas.BillRead])
def get_bills(
    reference: str | None = None,
    total_from: float | None = None,
    total_to: float | None = None,
    db: Session = Depends(deps.get_db)
    
) -> Any:
    """
    Retrieve items.
    """
    bills = crud.bill.filter(db=db, reference=reference, total_from=total_from, total_to=total_to)
    # bills = crud.bill.get_all(db=db)
    return bills


@router.post("/bills", response_model=schemas.Bill)
def create_bills(
    bill: schemas.BillCreate,
    db: Session = Depends(deps.get_db),
    
) -> Any:
    """
    Create bill.
    """
    total = bill.total
    total_subbills = sum([x.amount for x in bill.subbills])

    if total != total_subbills:
        raise HTTPException(status_code=400, detail="Bill total does not match subbills amount")

    subbills_exist = crud.subbill.exists(db=db, obj_in=bill.subbills)
    if len(subbills_exist) > 0:
        references = [x.reference for x in subbills_exist]
        raise HTTPException(status_code=400, detail="SubBills with reference already exist: " + ",".join(references))        
    bill = crud.bill.create_bill_with_subbill(db=db, obj_in=bill)

    return bill