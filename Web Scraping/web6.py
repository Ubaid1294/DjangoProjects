import requests
import re
import os

user = input("Enter the image name: ")
user_agent = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
}


url = f"https://www.google.com/search?sca_esv={user}&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeqDdErwP5rACeJAty2zADJjYuUnSkczEhozYdaq1wZrEheAY38UjnRKVLYFDREDmzz3c9iXgklNNbCtRRa3vQiDsiyngHMLCDiFcU14vRYFcn3hDvBtzesTsvCeqVb3Xc1wjI2MTiwr0UAtZV1SeaWYQtAHYGsCkaiqMHRd5y0JCw-KjIg&sa=X&ved=2ahUKEwjZ84me4baOAxXKyTgGHQmZJzkQtKgLKAF6BAgbEAE&biw=1536&bih=730&dpr=1.25"

response = requests.get(url=url, headers=user_agent).text
pattern = r"\[\"https://.*\.jpg\",[0-9]+,[+-9]+\]"

img = re.findall(pattern, response)

print(f"total: {len(img)}")
no_img = int(input("Enter number of images: to be downloaded :"))

if img:
    if not os.path.exists(user):
        os.mkdir(user)
        os.chdir(user)
    else:
        os.chdir(user)
    for img in img[:no_img]:
        img_url = eval(img)[0]
        # print(img_url)
        response = requests.get(url=img_url, headers=user_agent).content
        img_name = img.split("/")[-1]

        with open(img_name, "wb") as f:
            f.write(response)