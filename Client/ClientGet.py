import requests

endpoint = "http://127.0.0.1:8000/"

Responsee = requests.get(endpoint, json={"query": "Hello World"})

print(Responsee.status_code)