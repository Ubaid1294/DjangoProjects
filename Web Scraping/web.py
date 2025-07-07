# import urllib.request, urllib.parse, urllib.error
# url = urllib.request.urlopen('http://www.python.org')
#
# for line in url:
#     print(line.decode().strip())


import requests

url = "http://www.python.org"

response = requests.get(url=url)
print(response.request.headers)