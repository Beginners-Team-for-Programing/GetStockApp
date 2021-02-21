# print('Hello World!')
import requests
from bs4 import BeautifulSoup

url = "https://www.bloomberg.co.jp/quote/NKY:IND"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
nikkei = soup.select_one(".price")

print(nikkei)