import requests

url = "http://127.0.0.1:5000/login"
data = {
    "username": "admin",
    "password": "admin123"
}

r = requests.post(url, json=data)
print(r.text)
