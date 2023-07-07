#005380, 000270, 225570
import requests
from bs4 import BeautifulSoup

codes = [("005380","현대차"), ("000270","기아"), ("225570","넥슨게임즈")]
url = "https://finance.naver.com/item/sise.naver?code=%s"
prices = []

for code in codes :

  response = requests.get(url % code[0])

  html = response.text 
  soup = BeautifulSoup(html, "html.parser")
  price = soup.select_one("strong#_nowVal")
  prices.append((price.text, code[1]))

print(prices)