from pydantic import BaseModel
from decimal import Decimal


class StaffCreate(BaseModel):
    name:str
    role:str
    shift:str
    salary:Decimal
    

class StaffResponse(BaseModel):
    id:int
    name:str
    role:str
    shift:str
    salary:Decimal
     

    class Config():
        from_attributes= True
    