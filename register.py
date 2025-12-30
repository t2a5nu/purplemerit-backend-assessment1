import requests

url = "http://127.0.0.1:5000/register"
data = {
    "username": "admin",
    "password": "admin123",
    "role": "admin"
}

r = requests.post(url, json=data)
print(r.text)
