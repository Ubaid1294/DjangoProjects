import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

        self.response = requests.get(url = self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"
    def product_price(self):
        symbol = self.soup.find("span", {"class": "a-price-symbol"})
        price = self.soup.find("span", {"class": "a-price-whole"})

        if price is not None:
            return symbol.text + price.text
        else:
            return "Tag not found"

device = PriceTracer(url="https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5XW6TN?pd_rd_w=9sLPl&content-id=amzn1.sym.04c0c183-ba41-4b54-8093-1e68e6559c96&pf_rd_p=04c0c183-ba41-4b54-8093-1e68e6559c96&pf_rd_r=STH71CQMJ4K66XQ2DYC5&pd_rd_wg=V3PKi&pd_rd_r=1790a74d-0eb5-4b75-b257-141fe12b8630&pd_rd_i=B0CS5XW6TN&ref_=pd_hp_d_btf_unk_B0CS5XW6TN&th=1")

print(device.product_title())
print(device.product_price())

device2 = PriceTracer(url = "https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/ref=pd_sbs_d_sccl_2_2/260-9227451-9626505?pd_rd_w=ja995&content-id=amzn1.sym.6d240404-f8ea-42f5-98fe-bf3c8ec77086&pf_rd_p=6d240404-f8ea-42f5-98fe-bf3c8ec77086&pf_rd_r=HCXZGWQTAV2M05GN2NB1&pd_rd_wg=6n13G&pd_rd_r=94136a58-126b-4611-9aa6-deae43c1629e&pd_rd_i=B0CHX1W1XY&th=1")

print(device2.product_title())
print(device2.product_price())