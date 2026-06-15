import joblib
import numpy as np
import sklearn
from fastapi import FastAPI
from pydantic import BaseModel, Field

model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

def predict_charges(smoker, age, bmi):
    """
    Predice los cargos de seguro para nuevos valores.

    Args:
        smoker (int): 0 for 'no' smoker, 1 for 'yes' smoker.
        age (int): Age of the individual.
        bmi (float): BMI of the individual.

    Returns:
        float: Predicted insurance charges.
    """
    new_data = np.array([[smoker, age, bmi]])
    scaled_new_data = sc_x.transform(new_data)
    scaled_prediction = model.predict(scaled_new_data)
    prediction = sc_y.inverse_transform(scaled_prediction)

    return round(prediction[0][0],2)

app = FastAPI()

#schema validador
class Insurance(BaseModel):
    smoker: int
    age: int
    bmi: float
    
@app.get("/")
def home():
    return {"message":"Insurance API"}

@app.post("/insurance_price")
def insurance_price(insurance: Insurance):
    smoker = insurance.smoker
    age = insurance.age
    bmi = insurance.bmi
    charges = predict_charges(smoker,age,bmi)
    
    return{
        "smoker": smoker,
        "age": age,
        "bmi": bmi,
        "charges": charges
    }
    
