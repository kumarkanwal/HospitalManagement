from sqlalchemy.orm import Session 

from app.models.doctor import Doctor
from app.schemas.doctor import DocterCreate

def create_doctor(db: Session, doctor: DocterCreate):
    db_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        email=doctor.email,
        phone=doctor.phone,
        salary=doctor.salary

    )

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session,doctor_id: int):
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def update_doctor(db: Session, doctor_id: int, doctor: DocterCreate):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    db_doctor.name = doctor.name
    db_doctor.specialization = doctor.specialization
    db_doctor.email = doctor.email
    db_doctor.phone = doctor.phone
    db_doctor.salary = doctor.salary
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id:int):
    db_doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    db.delete(db_doctor)
    db.commit()
    return{"message": "Doctor deleted Successfully"}