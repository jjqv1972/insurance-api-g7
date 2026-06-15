import joblib
import numpy as np
import sklearn

# Cargar el modelo y los escaladores
loaded_model = joblib.load('./model/model.pkl')
loaded_scaler_x = joblib.load('./model/scaler_x.pkl')
loaded_scaler_y = joblib.load('./model/scaler_y.pkl')

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
    # Prepare the input features as a 2D array
    new_data = np.array([[smoker, age, bmi]])

    # Scale the new data using the loaded scaler_x
    scaled_new_data = loaded_scaler_x.transform(new_data)

    # Make a prediction using the loaded model
    scaled_prediction = loaded_model.predict(scaled_new_data)

    # Inverse transform the prediction to get the actual charges
    prediction = loaded_scaler_y.inverse_transform(scaled_prediction)

    return round(prediction[0][0],2)