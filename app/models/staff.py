from sqlalchemy import Column, String ,Numeric, Integer
from app.database import Base

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer, primary_key=True, index=True)
    name = Column( String, nullable=False)
    role = Column(String, nullable=False)
    shift = Column( String , nullable=False )
    salary = Column(Numeric(10,2), nullable=False)