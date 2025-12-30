import requests

token ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc2NzA4NTczNywianRpIjoiZjMzNDgwMGQtMDJmMi00NGEwLTk3YzItMTY5MzMwOWQ3NGQ1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwicm9sZSI6ImFkbWluIn0sIm5iZiI6MTc2NzA4NTczNywiZXhwIjoxNzY3MDg2NjM3fQ.pRIG9dsnYlTXnBG8IdDaq4KernQzFE4MWtH1tYTl6aA"

headers = {
    "Authorization": f"Bearer {token}"
}

url = "http://127.0.0.1:5000/profile"

r = requests.get(url, headers=headers)
print(r.json())
