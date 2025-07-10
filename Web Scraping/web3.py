import requests


post_url = "http://127.0.0.1:8000/post/"

#login credentials
username = "demo"
password = "12345"

payload = {
    "title": "Greetings",
    "content": "Welcome to python!",
}

response = requests.post(url=post_url, data=payload, auth=(username, password))
print(response.text)