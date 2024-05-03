import tkinter as tk
from bs4 import BeautifulSoup
import requests
url_usd = 'https://www.google.com/finance/quote/USD-TRY?hl=tr'
page = requests.get(url_usd)
html_page = BeautifulSoup(page.content, "html.parser")
dollar = html_page.find("div", class_="YMlKec fxKbKc").getText()
casteddollar = float(dollar.replace(",", "."))
print(casteddollar)