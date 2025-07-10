import requests

url = "http://127.0.0.1:8000/post/"

#login credentials
username = "demo"
password = "12345"

params = {
    "offset": 10,
}

response = requests.get(url=url, params=params, auth=(username, password))

print(response.text)
print(response.url)