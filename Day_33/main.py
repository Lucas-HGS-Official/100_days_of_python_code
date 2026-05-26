import datetime

import requests

LAT_SP = -23.533773
LNG_SP = -46.625290


def is_iss_above():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()

    data_iss = response_iss.json()

    iss_lng = float(data_iss["iss_position"]["longitude"])
    iss_lat = float(data_iss["iss_position"]["latitude"])

    if (LAT_SP - 5 <= iss_lat <= LAT_SP + 5) and (LNG_SP - 5 <= iss_lng <= LNG_SP + 5):
        return True
    else:
        return False


def is_night():
    param = {
        "lat": float(LAT_SP),
        "lng": float(LNG_SP),
        "formatted": 0,
    }
    response_sunrise = requests.get("https://api.sunrise-sunset.org/json", params=param)
    response_sunrise.raise_for_status()

    data_sunrise_sunset = response_sunrise.json()

    sunrise_hour = int(data_sunrise_sunset["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data_sunrise_sunset["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.datetime.now().hour

    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True
    else:
        return False


if __name__ == "__main__":
    if is_iss_above() and is_night():
        print("it is")
    else:
        print("no")
