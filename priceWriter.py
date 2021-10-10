import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime, date

URL = 'https://www.amazon.es/gp/product/B00YUIM2J0/ref=ox_sc_saved_title_2?smid=A1AT7YVPFBWXBL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}

#Setting up the files and date
log = open("log.txt", 'w')
now = datetime.now()
today = date.today()

def priceCheck():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id = "priceblock_ourprice").get_text()
    priceWithDot = price.replace(",", ".")
    convertedPrice = float(priceWithDot[0:5])
    currentDate = today.strftime("%d/%m/%Y")
    currentTime = now.strftime("%H:%M:%S")
    log.write(str(currentDate) + " " + str(currentTime) + " " + str(convertedPrice) + "\n")
    print("Written!")

while True:
   priceCheck()
   sleep(5)