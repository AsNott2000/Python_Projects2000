import tkinter as tk
from bs4 import BeautifulSoup
import requests

#api data extraction
url_usd = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
url_euro = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
url_sterlin = "https://www.google.com/finance/quote/GBP-TRY?hl=tr"
page_usd = requests.get(url_usd)
page_euro = requests.get(url_euro)
page_sterlin = requests.get(url_sterlin)

html_usd = BeautifulSoup(page_usd.content, "html.parser")
html_euro = BeautifulSoup(page_euro.content, "html.parser")
html_sterlin = BeautifulSoup(page_sterlin.content, "html.parser")

euro = html_euro.find("div", class_="YMlKec fxKbKc").getText()
dollar = html_usd.find("div", class_="YMlKec fxKbKc").getText()
sterlin = html_sterlin.find("div", class_="YMlKec fxKbKc").getText()

casted_dollar = float(dollar.replace(",", "."))
casted_euro = float(euro.replace(",", "."))
casted_sterlin = float(sterlin.replace(",", "."))

#eger euro usd veya usd euro hesaplanmak isterse ikisini birbirine boleriz boylece paritesini bulmus oluruz.
#ornegin dolar 4 euro 6 tl ise, euro/usd= 6/4 olur.


#ui
ui = tk.Tk()
ui.title("Currency Converter 2000")



ui.mainloop()
