import requests
import datetime as dt
import os

headers = {
    "x-app-id": "7a657c0e",
    "x-app-key": "",
}

body = {
    "query": input("what excercise did you do today? "),
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=body)

data = response.json()

print(data)


today = dt.datetime.now()

os.environ["TOKEN"] = input("please provide token ")
TOKEN = os.environ.get("TOKEN")

header_2= {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

body_2 = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M"),
        "exercise": data["exercises"][0]["name"],
        "duration": data["exercises"][0]["duration_min"],
        "calories": data["exercises"][0]["nf_calories"],
    }
}

response_2 = requests.post(url="https://api.sheety.co/cbeb1d74694f092e37df108efb9377c0/myWorkouts/workouts", headers=header_2, json=body_2)
print(response_2)
