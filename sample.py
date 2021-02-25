import requests
from bs4 import BeautifulSoup
import time
import os
from plyer import notification


# os判別
if os.name == 'nt':
    print('on Windows')
    notification.notify(
        title = "デスクトップ通知",
        message="windows",
        timeout=5
    )
elif os.name == 'posix':
    print('on Mac or Linux')
    notification.notify(
        title = "デスクトップ通知",
        message="Mac or Linux",
        timeout=5
    )

url = "https://www.bloomberg.co.jp/quote/NKY:IND"

for i in range(1000):
    print(time.time())
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    nikkei = soup.select_one(".price")
    print(nikkei)
    time.sleep(1)