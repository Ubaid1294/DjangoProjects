import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')
    tag = soup.find("div",{"id":"mp-right","class":"MainPageBG mp-box"})
    h = tag.find_all("h2")
    content = [h2.text for h2 in h]
    print(content)
    # print(h)

    with open("wiki.csv", "a") as csvfile:
        csv_write = csv.writer(csvfile)
        csv_write.writerow(content)

Extract(url="https://en.wikipedia.org/wiki/Main_Page")
