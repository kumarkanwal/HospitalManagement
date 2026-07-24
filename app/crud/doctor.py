from sqlalchemy.orm import Session 

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

def create_doctor(db: Session, doctor: DoctorCreate):
    db_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        email=doctor.email,
        phone=doctor.phone,
        salary=doctor.salary

    )

    try:
        db.add(db_doctor)
        db.commit()
        db.refresh(db_doctor)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email or phone already exists")
    return db_doctor

def get_doctor(db: Session,doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def update_doctor(db: Session, doctor_id: int, doctor: DoctorCreate):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    db_doctor.name = doctor.name
    db_doctor.specialization = doctor.specialization
    db_doctor.email = doctor.email
    db_doctor.phone = doctor.phone
    db_doctor.salary = doctor.salary
    try:
        db.commit()
        db.refresh(db_doctor)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email or phone already exists")
    return db_doctor

def delete_doctor(db: Session, doctor_id:int):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    db.delete(db_doctor)
    db.commit()
    return{"message": "Doctor deleted Successfully"}