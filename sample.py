# print('Hello World!')
import requests
from bs4 import BeautifulSoup
import time

url = "https://www.bloomberg.co.jp/quote/NKY:IND"

for i in range(1000):
    print(time.time())
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    nikkei = soup.select_one(".price")
    print(nikkei)
    time.sleep(1)