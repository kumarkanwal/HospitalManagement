from fastapi import FastAPI
from sqlalchemy import text

from app.config import settings
from app.database import engine

from app.routes import doctor, patient, staff

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.include_router(doctor.router)              
app.include_router(patient.router)
app.include_router(staff.router)


@app.on_event("startup")
def check_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            print("✅ Database connected")
    except Exception as e:
        print(f"❌ Connection failed: {e}")


@app.get("/")
def health_check():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }