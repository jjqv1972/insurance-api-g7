import joblib
import numpy as np
import sklearn

# Cargar el modelo y los escaladores
model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

print("modelos cargados...")

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

# Ejemplo de uso:
# Supongamos un no fumador de 30 años con un IMC de 25
new_smoker = 0  # no smoker
new_age = 30
new_bmi = 25.0
predicted_charge = predict_charges(new_smoker, new_age, new_bmi)
print(f'Predicted insurance charge for a non-smoker, 30 years old, with BMI 25: {predicted_charge:.2f}')