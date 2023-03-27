import requests

endpoint = "http://127.0.0.1:8000/api/"

Responsee = requests.post(endpoint, json={"title":"Dora the Explorer", "content": "Adventure Island", "context": "University 2", "price": 12000})

# print(Responsee.status_code)
json_ = Responsee.json()
print(json_)