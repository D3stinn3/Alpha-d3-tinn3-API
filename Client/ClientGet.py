import requests

endpoint = "http://127.0.0.1:8000/api/"

Responsee = requests.post(endpoint, json={"title":"Maisha", "content": "Njia Panda", "context": "Grade 2", "price": 3000})

# print(Responsee.status_code)
json_ = Responsee.json()
print(json_)