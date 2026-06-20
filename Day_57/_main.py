import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


def main():
    if __name__ == "__main__":
        app.run(debug=True)


@app.route("/")
def home():
    rand_num = random.randint(1, 10)
    return render_template("index.html", num=rand_num)


@app.route("/guess/<name>")
def guess_name(name: str):
    agify_url = "https://api.agify.io"
    agify_response = requests.get(agify_url, params={"name": name})
    agify_response.raise_for_status()
    age_data = agify_response.json()
    age = age_data["age"]

    genderize_url = "https://api.genderize.io"
    genderize_response = requests.get(genderize_url, params={"name": name})
    genderize_response.raise_for_status()
    gender_data = genderize_response.json()
    gender = gender_data["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


main()
