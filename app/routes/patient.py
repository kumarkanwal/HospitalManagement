from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.patient import PatientCreate, PatientResponse
from app.crud.patient import (
    create_patient,
    get_patient,
    get_all_patients,
    update_patient,
    delete_patient
)

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post('/',response_model=PatientResponse)
def create(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)

@router.get('/',response_model=list[PatientResponse] )
def get_all(db:Session = Depends(get_db)):
    return get_all_patients(db)

@router.get("/{patient_id}", response_model=PatientResponse)
def get_one(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db,patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="patient not Found")
    return patient

@router.put("/{patient_id}", response_model=PatientResponse)
def update(patient_id: int, patient:PatientCreate, db: Session = Depends(get_db) ):
    return update_patient(db,patient_id,patient)

@router.delete("/{patient_id}")
def delete(patient_id: int, db:Session = Depends(get_db)):
    return delete_patient(db,patient_id)