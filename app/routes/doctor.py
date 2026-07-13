from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.doctor import DoctorCreate, DoctorResponse
from app.crud.doctor import (
    create_doctor,
    get_doctor,
    get_all_doctors,
    update_doctor,
    delete_doctor
)

router = APIRouter(prefix="/doctors", tags=["Doctors"])

@router.post('/',response_model=DoctorResponse)
def create(doctor: DoctorCreate, db: Session = Depends(get_db)):
    return create_doctor(db, doctor)


@router.get("/", response_model=list[DoctorResponse])
def get_all(db:Session = Depends(get_db)):
    return get_all_doctors(db)

@router.get("/{doctor_id}", response_model=DoctorResponse )
def get_one(doctor_id: int, db:Session = Depends(get_db)):
    doctor = get_doctor(db,doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.put("/{doctor_id}", response_model=DoctorResponse)
def update(doctor_id: int, doctor: DoctorCreate, db: Session = Depends(get_db) ):
    return update_doctor(db,doctor_id,doctor)


@router.delete("/{doctor_id}")
def delete(doctor_id: int, db: Session = Depends(get_db) ):
    return delete_doctor(db,doctor_id)

