from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Insurance
from ml_model import predict_charges

from schemas import (
    InsuranceCreate,
    InsuranceResponse
)

router = APIRouter(
    prefix="/insurance",
    tags=["Insurance"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/",response_model=InsuranceResponse)
def create_insurance(data: InsuranceCreate,db: Session = Depends(get_db)):
    smoker = data.smoker
    age = data.age
    bmi = data.bmi
    
    charges = predict_charges(smoker,age,bmi)
    
    new_insurance = Insurance(
        smoker = smoker,
        age = age,
        bmi = bmi,
        charges = charges
    )
    
    db.add(new_insurance)
    db.commit()
    db.refresh(new_insurance)

    return new_insurance

@router.get("/",response_model=list[InsuranceResponse])
def get_insurance(db: Session = Depends(get_db)):
    return db.query(Insurance).all() # select * from insurance

@router.put("/{insurance_id}", response_model=InsuranceResponse)
def update_insurance(
    insurance_id: int,
    data: InsuranceCreate,
    db: Session = Depends(get_db)
):
    insurance = db.query(Insurance).filter(Insurance.id == insurance_id).first()

    if not insurance:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    charges = predict_charges(data.smoker, data.age, data.bmi)

    insurance.smoker = data.smoker
    insurance.age = data.age
    insurance.bmi = data.bmi
    insurance.charges = charges

    db.commit()
    db.refresh(insurance)

    return insurance


@router.delete("/{insurance_id}")
def delete_insurance(insurance_id: int, db: Session = Depends(get_db)):
    insurance = db.query(Insurance).filter(Insurance.id == insurance_id).first()

    if not insurance:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    db.delete(insurance)
    db.commit()

    return {"message": "Registro eliminado correctamente"}