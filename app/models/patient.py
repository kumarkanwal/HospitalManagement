from sqlalchemy import Column, Integer, String , Date, ForeignKey
from app.database import Base



class Patient(Base):
    __tablename__= "patients"
   

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    disease = Column(String, nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    admission_date = Column(Date, nullable=False)

