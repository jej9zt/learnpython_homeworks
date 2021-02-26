import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
res = requests.get(url).text
soup = BeautifulSoup(res, "html.parser")

b = soup.find('b', text='Maps & Images')
if b:
    lat_long = b.find_next().text

