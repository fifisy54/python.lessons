import requests
from bs4 import BeautifulSoup
from datetime import datetime
#29/09/2019
url = "https://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
print(response.content)

soup = BeautifulSoup(response.content, "lxml")

def get_course(id):
    valute = soup.find("valute", {"id": id})
    return f"За {valute.nominal.text} {valute.nominal.next_sibling.text} дают {valute.value.text} рублей"

valutes = soup.find_all("valute")

for x in valutes:
    print(get_course(x["id"]))


