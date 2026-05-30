import os

import requests
from twilio.rest import Client

OWM_API_KEY = os.environ.get("OWM_API_KEY")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")

TWILIO_SENDER = os.environ.get("TWILIO_SENDER")
TWILIO_RECEIVER = os.environ.get("TWILIO_RECEIVER")

LAT_SP = os.environ.get("LAT_SP")
LNG_SP = os.environ.get("LNG_SP")


if __name__ == "__main__":
    is_raining = False

    owm_params = {"lat": LAT_SP, "lon": LNG_SP, "appid": OWM_API_KEY, "cnt": 4}
    response = requests.get(OWM_ENDPOINT, params=owm_params)
    response.raise_for_status()

    weather_data = response.json()
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < 700:
            is_raining = True

    if is_raining:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            # messaging_service_sid="MG3392a984ec5e2ad142b5c4d3686bf0b5",
            body="It will rain today!",
            from_=TWILIO_SENDER,
            to=TWILIO_RECEIVER,
        )
        print(message.status)
    else:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            # messaging_service_sid="MG3392a984ec5e2ad142b5c4d3686bf0b5",
            body="Ahoy 👋",
            from_=TWILIO_SENDER,
            to=TWILIO_RECEIVER,
        )
        print(message.status)
