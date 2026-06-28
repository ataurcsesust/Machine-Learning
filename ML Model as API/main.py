from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Create FastAPI app
app = FastAPI()

# Load the trained model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# Input data model
class ModelInput(BaseModel):
    pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# Prediction API
@app.post("/diabetes_prediction")
def diabetes_prediction(input_parameters: ModelInput):

    input_list = [
        input_parameters.pregnancies,
        input_parameters.Glucose,
        input_parameters.BloodPressure,
        input_parameters.SkinThickness,
        input_parameters.Insulin,
        input_parameters.BMI,
        input_parameters.DiabetesPedigreeFunction,
        input_parameters.Age
    ]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        result = "The person is not diabetic"
    else:
        result = "The person is diabetic"

    return {
        "prediction": result
    }