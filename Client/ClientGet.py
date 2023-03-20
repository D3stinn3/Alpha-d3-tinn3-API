import requests

endpoint = "http://127.0.0.1:8000/api"

Responsee = requests.get(endpoint, json={"query":"Hello World"})

# print(Responsee.status_code)
json_ = Responsee.json()
print(json_)