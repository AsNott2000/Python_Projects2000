import tkinter as tk

# Toplama işlemi
def toplama(x, y):
    return x + y

# Çıkarma işlemi
def cikarma(x, y):
    return x - y

# Çarpma işlemi
def carpma(x, y):
    return x * y

# Bölme işlemi
def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    else:
        return x / y


# Ana pencereyi oluştur
root = tk.Tk()
root.title("Tkinter Örneği")

# sayilar
sayi1 = tk.Entry(root)
sayi1.pack()
etiket1 = tk.Label(root, text="sayi 1'i giriniz")
etiket1.pack()

sayi2 = tk.Entry(root)
sayi2.pack()
etiket2 = tk.Label(root, text="sayi 2'yi giriniz")
etiket2.pack()

def cast_type_num1():
    text1 = sayi1.get()
    try:
        num1 = int(text1)  
        return num1
    except:
        print("This is not number")
        return None
def cast_type_num2():
    text2 = sayi2.get()
    try:
        num2 = int(text2)
        return num2
    except:
        print("This is not number")
        return None

# Düğme

aa = cast_type_num1()
bb = cast_type_num2()

topla_btn = tk.Button(root, text="Topla", command=toplama(aa, bb))
topla_btn.pack()

carpma_btn = tk.Button(root, text="Carp", command=carpma(aa, bb))
carpma_btn.pack()

bolme_btn = tk.Button(root, text="Bol", command=bolme(aa, bb))
bolme_btn.pack()

cikarma_btn = tk.Button(root, text="Cikar", command=cikarma(aa, bb))
cikarma_btn.pack()

# Ana döngüyü başlat
root.mainloop()
