from fastapi import FastAPI
from database import engine
from models import Base
from routers import insurance


app = FastAPI(
    title="Insurance API con FastAPI",
    description="API para predicción de primas de seguro usando Machine Learning, FastAPI y SQLAlchemy",
    version="1.0.0"
)

app.include_router(insurance.router)

@app.get("/")
def index():
    return {
        "title": "FASTAPI INSURANCE API VERSION 1.0",
        "message": "Bienvenido a mi API"
    }
    
#Base.metadata.create_all(engine)