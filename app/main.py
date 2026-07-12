from fastapi import FastAPI

from app.config import Settings

app = FastAPI(
    title=Settings.APP_NAME,
    version=Settings.APP_VERSION,
    debug=Settings.DEBUG,
)


@app.get("/")
def health_check():
    return {
        "app" : Settings.APP_NAME,
        "version": Settings.APP_VERSION,
        "status" : 'running'
    }

