from sqlalchemy.orm import Session

from app.models.staff import Staff
from app.schemas.staff import StaffCreate


def create_staff(db: Session, staff: StaffCreate):
    db_staff = Staff(
        name = staff.name,
        role = staff.role,
        shift = staff.shift,
        salary = staff.salary

    )

    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def get_staff(db : Session, staff_id: int):
    return db.query(Staff).filter(Staff.id == staff_id).first()

def get_all_staff(db: Session):
    return db.query(Staff).all()

def update_staff(db: Session, staff: StaffCreate):
    db_staff = db.query(Staff).filter(Staff.id == staff_id).first()
    db_staff.name = staff.name
    db_staff.role = staff.role
    db_staff.shift = staff.shift
    db_staff.salary = staff.salary

    db.commit()
    db.refresh(db_staff)
    return db_staff


def delete_staff(db: Session, staff_id: int):
    
    db_staff = db.query(Staff).filter(Staff.id == staff_id).first()
    db.delete(db_staff)
    db.commit()
    return {"message": "staff deleted Successfully"}
