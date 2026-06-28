import requests

url = "https://obscure-slogan-swear.ngrok-free.dev/diabetes_prediction"

input_data = {
    "Pregnancies": 1,
    "Glucose": 89,
    "BloodPressure": 66,
    "SkinThickness": 23,
    "Insulin": 94,
    "BMI": 28.1,
    "DiabetesPedigreeFunction": 0.167,
    "Age": 21
}

response = requests.post(url, json=input_data)

print(response.status_code)
print(response.json())