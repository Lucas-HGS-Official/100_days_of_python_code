import os
from datetime import datetime

import requests

PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USER = "lhgs"
PIXELA_GRAPHID = "d0loc0graph"
PIXELA_ENDPOINT = "https://pixe.la/v1/users/"
PIXELA_GRAPH_ENDPOINT = PIXELA_ENDPOINT + PIXELA_USER + "/graphs/"
PIXELA_PIXEL_ENDPOINT = PIXELA_GRAPH_ENDPOINT + PIXELA_GRAPHID


if __name__ == "__main__":
    # Generate Pixela user #
    # pixela_params = {
    #     "token": PIXELA_TOKEN,
    #     "username": "lhgs",
    #     "agreeTermsOfService": "yes",
    #     "notMinor": "yes",
    # }
    # pixela_response = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
    # print(pixela_response.text)
    # https://pixe.la/@lhgs
    #########################

    # Generate a graph
    # pixela_params = {
    #     "id": "d0loc0graph",
    #     "name": "Daily Lines of Code",
    #     "unit": "LOC",
    #     "type": "int",
    #     "color": "momiji",
    # }
    # headers = {
    #     "X-USER-TOKEN": PIXELA_TOKEN,
    # }
    # pixela_response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=pixela_params, headers=headers)
    # print(pixela_response.text)
    # # https://pixe.la/v1/users/lhgs/graphs/d0loc0graph.html
    #########################

    today = datetime.now()

    pixela_params = {
        "date": str(today.strftime("%Y%m%d")),
        "quantity": "53",
    }
    headers = {
        "X-USER-TOKEN": PIXELA_TOKEN,
    }
    pixela_response = requests.post(url=PIXELA_PIXEL_ENDPOINT, json=pixela_params, headers=headers)
    print(pixela_response.text)
