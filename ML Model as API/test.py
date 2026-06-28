import requests

url = "http://127.0.0.1:8000/diabetes_prediction"

input_data = {
    "pregnancies": 1,
    "Glucose": 89,
    "BloodPressure": 66,
    "SkinThickness": 23,
    "Insulin": 94,
    "BMI": 28.1,
    "DiabetesPedigreeFunction": 0.167,
    "Age": 21
}

response = requests.post(url, json=input_data)

print(response.json())
