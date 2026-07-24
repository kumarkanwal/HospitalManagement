from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

def create_patient(db: Session, patient: PatientCreate):
    doctor = db.query(Doctor).filter(Doctor.id == patient.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=400, detail="Doctor does not exist")
    db_patient = Patient(
        name = patient.name,
        age = patient.age,
        gender = patient.gender,
        disease = patient.disease,
        doctor_id = patient.doctor_id,
        admission_date = patient.admission_date

    )

    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db:Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_all_patients(db:Session):
    return db.query(Patient).all()

def update_patient(db:Session,patient_id: int, patient: PatientCreate ):

    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    db_patient.name = patient.name
    db_patient.age = patient.age
    db_patient.gender = patient.gender
    db_patient.disease = patient.disease
    db_patient.doctor_id = patient.doctor_id
    db_patient.admission_date = patient.admission_date

    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db:Session, patient_id: int):
    db_patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(db_patient)
    db.commit()
    return{"message": "Patient deleted Successfully"}
