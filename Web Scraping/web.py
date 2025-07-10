# import urllib.request, urllib.parse, urllib.error
# url = urllib.request.urlopen('http://www.python.org')
#
# for line in url:
#     print(line.decode().strip())


import requests

url = "http://127.0.0.1:8000/picture/images/471414818_122115221804619572_2336895659911069942_n_fvs2RS7.jpg"
user = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
}
response = requests.get(url=url,headers=user)
pic = response.content

f = open("471414818_122115221804619572_2336895659911069942_n_fvs2RS7.jpg","wb")
f.write(pic)