import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

#Functions
def _currency():
    _entry = float(_input.get())
    if cbox_input.get() == 'Usd' and cbox_output.get() == 'Tl':
        curency_dollar = _entry*casted_dollar
        label_result.config(text = round(curency_dollar, 4))
    elif cbox_input.get() == 'Euro' and cbox_output.get() == 'Tl':
        curency_euro = _entry * casted_euro
        label_result.config(text = round(curency_euro, 4))
    elif cbox_input.get() == 'Gbp' and cbox_output.get() == 'Tl':
        curency_sterlin = _entry * casted_gbp
        label_result.config(text=round(curency_sterlin, 4))
    elif cbox_input.get() == 'Usd' and cbox_output.get() == 'Euro':
        curency_dollar = casted_dollar / casted_euro
        label_result.config(text = round(curency_dollar, 4))
    elif cbox_input.get() == 'Usd' and cbox_output.get() == 'Gbp':
        curency_dollar= casted_dollar / casted_gbp
        label_result.config(text=round(curency_dollar, 4))
    elif cbox_input.get() == 'Usd' and cbox_output.get() == 'Usd':
        curency_dollar = _entry
        label_result.config(text = round(curency_dollar, 4))
    elif cbox_input.get() == 'Euro' and cbox_output.get() == 'Usd':
        curency_euro = casted_euro / casted_dollar
        label_result.config(text=round(curency_euro, 4))
    elif cbox_input.get() == 'Euro' and cbox_output.get() == 'Gbp':
        curency_euro = casted_euro / casted_gbp
        label_result.config(text = round(curency_euro, 4))
    elif cbox_input.get() == 'Euro' and cbox_output.get() == 'Euro':
        curency_euro = _entry
        label_result.config(text=round(curency_euro, 4))
    elif cbox_input.get() == 'Gbp' and cbox_output.get() == 'Usd':
        curency_sterlin = casted_gbp / casted_dollar
        label_result.config(text = round(curency_sterlin, 4))
    elif cbox_input.get() == 'Gbp' and cbox_output.get() == 'Euro':
        curency_sterlin = casted_gbp / casted_euro
        label_result.config(text=round(curency_sterlin, 4))
    elif cbox_input.get() == 'Gbp' and cbox_output.get() == 'Gbp':
        curency_sterlin = _entry
        label_result.config(text=round(curency_sterlin, 4))
    elif cbox_input.get() == 'Tl' and cbox_output.get() == 'Usd':
        curency_tl = _entry / casted_dollar
        label_result.config(text=round(curency_tl, 4))
    elif cbox_input.get() == 'Tl' and cbox_output.get() == 'Euro':
        curency_tl = _entry /  casted_euro
        label_result.config(text=round(curency_tl, 4))
    elif cbox_input.get() == 'Tl' and cbox_output.get() == 'Tl':
        curency_tl = _entry
        label_result.config(text=round(curency_tl, 4))
    elif cbox_input.get() == 'Tl' and cbox_output.get() == 'Gbp':
        curency_tl = _entry / casted_gbp
        label_result.config(text=round(curency_tl, 4))


#api data extraction
url_usd = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
url_euro = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
url_gbp = "https://www.google.com/finance/quote/GBP-TRY?hl=tr"
page_usd = requests.get(url_usd)
page_euro = requests.get(url_euro)
page_gbp = requests.get(url_gbp)

html_usd = BeautifulSoup(page_usd.content, "html.parser")
html_euro = BeautifulSoup(page_euro.content, "html.parser")
html_gbp = BeautifulSoup(page_gbp.content, "html.parser")

euro = html_euro.find("div", class_="YMlKec fxKbKc").getText()
dollar = html_usd.find("div", class_="YMlKec fxKbKc").getText()
gbp = html_gbp.find("div", class_="YMlKec fxKbKc").getText()

casted_dollar = float(dollar.replace(",", "."))
casted_euro = float(euro.replace(",", "."))
casted_gbp = float(gbp.replace(",", "."))

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
label_output = tk.Label(ui, text="Result : ", font="Times 17")
label_output.place(x=50, y=170)

n = tk.StringVar()
cbox_input = ttk.Combobox(ui, width=10, textvariable=n, font="Times 15")
cbox_input['values'] = ('Tl','Usd', 'Euro', 'Gbp')
cbox_input.place(x=70, y=40)
cbox_input.current(1)

m = tk.StringVar()
cbox_output = ttk.Combobox(ui, width=10, textvariable=m, font="Times 15")
cbox_output['values'] = ('Tl', 'Usd', 'Euro', 'Gbp')
cbox_output.place(x=220, y=40)
cbox_output.current(0)

currency = tk.Button(ui, text="Currency", font="Times 17", command=_currency)
currency.place(x=75, y=250)

ui.mainloop()
