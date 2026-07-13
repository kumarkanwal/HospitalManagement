from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session


from app.database import get_db
from app.schemas.staff import StaffCreate, StaffResponse
from app.crud.staff import (
    create_staff,
    get_staff,
    get_all_staff,
    update_staff,
    delete_staff
)


router = APIRouter(prefix="/staffs", tags=["staff"])

@router.post('/', response_model=StaffResponse)
def create(staff: StaffCreate, db: Session = Depends(get_db)):
    return create_staff(db,staff)

@router.get('/', response_model=list[StaffResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_staff(db)

@router.get("/{staff_id}", response_model=StaffResponse )
def get_one(staff_id: int, db:Session = Depends(get_db)):
    staff = get_staff(db,staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff
    
@router.put("/{staff_id}", response_model=StaffResponse)
def update(staff_id: int, staff: StaffCreate, db:Session = Depends(get_db)):
    return update_staff(db, staff_id,staff)

@router.delete("/{staff_id}")
def delete(staff_id: int, db: Session = Depends(get_db)):
    return delete_staff(db,staff_id)

