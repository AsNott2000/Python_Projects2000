import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

#Functions
def _currency():
    _entry = float(_input.get())
    if cbox.get() == 'Usd':
        curency_dollar = _entry*casted_dollar
        label_result.config(text = round(curency_dollar, 2))
    elif cbox.get() == 'Euro':
        curency_euro = _entry * casted_euro
        label_result.config(text = round(curency_euro, 2))
    elif cbox.get() == 'Sterlin':
        curency_sterlin = _entry * casted_sterlin
        label_result.config(text=round(curency_sterlin, 2))


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
ui.geometry("475x320+600+250")
ui.resizable(False, False)

_input = tk.Entry(ui, width=25, font="Times 12 bold")
_input.place(x=150, y=110)

label = tk.Label(ui, text="Price : ", font="Times 17")
label.place(x=50, y=105)
label_result = tk.Label(ui, text="", font="Times 17")
label_result.place(x=150, y=170)
label_tl = tk.Label(ui, text="Result : ", font="Times 17")
label_tl.place(x=50, y=170)

n = tk.StringVar()
cbox = ttk.Combobox(ui, width=27, textvariable=n, font="Times 15")
cbox['values'] = ('Usd', 'Euro', 'Sterlin')
cbox.place(x=70, y=40)
cbox.current(0)

currency = tk.Button(ui, text="Currency", font="Times 17", command=_currency)
currency.place(x=75, y=250)
ui.mainloop()
