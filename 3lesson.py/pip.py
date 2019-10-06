import requests
from bs4 import BeautifulSoup

def temp(html):
    return html.find("span", {"class":"temp__value"}).text
url = "https://yandex.ru/pogoda/moscow"
response = requests.get(url)
html = BeautifulSoup(response.content, "lxml")
print (temp(html))

def condition(html):
    return html.find("div", {"class":"link__condition"}).text
print (condition(html))

hours = 3

sunset = 18

sunrise = 6

if hourse >= sunrise and hourse <= sunset
    print("На улице солнце")