# https://finance.naver.com/item/sise.naver?code=005380
# 종목과 가격을 가져올거다

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver?code=005380"
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, "html.parser")
price = soup. select_one("strong#_nowVal")
print(price.text)