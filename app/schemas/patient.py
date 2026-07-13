from pydantic import BaseModel
from decimal import Decimal
from datetime import date

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    disease: str
    doctor_id: int
    admission_date: date

class PatientResponse(BaseModel):
    id : int
    name: str
    age: int
    gender: str
    disease: str
    doctor_id: int
    admission_date: date

    


    class Config():
        from_attributes = True

