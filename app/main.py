from fastapi import FastAPI

from app.config import Settings
from app.database import engine

app = FastAPI(
    title=Settings.APP_NAME,
    version=Settings.APP_VERSION,
    debug=Settings.DEBUG,
)
@app.on_event("startup")
def check_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
            print("✅ Database connected")
    except Exception as e:
        print(f"❌ Connection failed: {e}")

        
@app.get("/")
def health_check():
    return {
        
        "app" : Settings.APP_NAME,
        "version": Settings.APP_VERSION,
        "status" : 'running'
    }



