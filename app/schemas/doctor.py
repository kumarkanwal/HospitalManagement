from pydantic import BaseModel
from decimal import Decimal

class DoctorCreate(BaseModel):
    name:str
    specialization: str
    email: str
    phone: str
    salary: Decimal

class DoctorResponse(BaseModel):
    id:int
    name: str
    specialization : str
    email: str
    phone : str
    salary: Decimal

    class Config:
        from_attributes = True    

         
