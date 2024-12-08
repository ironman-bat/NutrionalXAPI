import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32


APP_ID = os.environ["23423432lk4l234l234m234"]
API_KEY = os.environ["1oi3j12ol3j4jlk23n4l32"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = os.environ[
    "110923i12i312io3j123jj12l3j"]


for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    """
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    """


    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["Malcore_55"],
            os.environ["abc12345"],
        )
    )


    """
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )    
    """
    print(f"Sheety Response: \n {sheet_response.text}")
