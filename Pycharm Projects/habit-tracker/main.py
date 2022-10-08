import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "moienmm"
TOKEN = "mohsenimofidi"
GRAPH_ID = "graph1"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


#response = requests.post(url=pixela_endpoint, json=user_parameters)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name":"Water Graph",
    "unit": "Litr",
    "type": "float",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

#graph_response = requests.post(graph_endpoint, json=graph_parameters, headers=headers)
#print(graph_response.text)

today = datetime.now()

pixel_graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How much water have you drunk today?")
}

pixel_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_graph = requests.post(pixel_graph_endpoint, json=pixel_graph_params, headers=headers)
print(pixel_graph.text)
#update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
#update_parameter = {
#    "quantity": "18.5"
#}
#response_update = requests.put(url=update_endpoint, json=update_parameter, headers=headers)
#print(#response_update.text)