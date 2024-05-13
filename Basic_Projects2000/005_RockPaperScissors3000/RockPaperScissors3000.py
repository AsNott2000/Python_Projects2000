import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
import random
from tkinter import messagebox

fence = tk.Tk()
fence.geometry("518x300")
fence.resizable(width= False, height= False)

moves = [
            "rock",
            "paper",
            "scissors"
        ]
kira_count = 0
user_count = 0
def _rock():
    moveKira = random.choice(moves)
    if moveKira == "rock":
        messagebox.showinfo("INFO", "TIE"+"\n\nKira's Move= "+ moveKira)
    elif moveKira == "paper":
        messagebox.showinfo("INFO", "KIRA WON"+"\n\nKira's Move= "+ moveKira)
    else:
        messagebox.showinfo("INFO", "YOU WON"+"\n\nKira's Move= "+ moveKira)
def _paper():
    moveKira = random.choice(moves)
    if moveKira == "rock":
        messagebox.showinfo("INFO", "YOU WIN"+"\n\nKira's Move= "+ moveKira)
    elif moveKira == "paper":
        messagebox.showinfo("INFO", "TIE"+"\n\nKira's Move= "+ moveKira)
    else:
        messagebox.showinfo("INFO", "KIRA WIN"+"\n\nKira's Move= "+ moveKira)
def _scissors():
    moveKira = random.choice(moves)
    if moveKira == "rock":
        messagebox.showinfo("INFO", "KIRA WON"+"\n\nKira's Move= "+ moveKira)
    elif moveKira == "paper":
        messagebox.showinfo("INFO", "YOU WON"+"\n\nKira's Move= "+ moveKira)
    else:
        messagebox.showinfo("INFO", "TIE"+"\n\nKira's Move= "+ moveKira)

#Rock Button
rock_img = Image.open('./img/rock.png')
RockWidth, RockHeight = rock_img.size

rock_w = int(RockWidth/3)
rock_h = int(RockHeight/3)

sizedRock = rock_img.resize((rock_w,rock_h))

Rock_Pimage = PhotoImage(sizedRock)

button_Rock = tk.Button(fence, image=Rock_Pimage, command= _rock)
button_Rock.place(x=0,y=0)

#Paper Button
paper_img = Image.open('./img/paper.png')
PaperWidth, PaperHeight = paper_img.size

paper_w = int(PaperWidth/3)
paper_h = int(PaperHeight/3)

sizedPaper = paper_img.resize((paper_w,paper_h))

Paper_Pimage = PhotoImage(sizedPaper)

button_Paper = tk.Button(fence, image=Paper_Pimage, command=_paper)
button_Paper.place(x=175,y=0)

#Scissors Button
scissors_img = Image.open('./img/scissors.png')
ScissorsWidth, ScissorsHeight = scissors_img.size

scissors_w = int(ScissorsWidth/3)
scissors_h = int(ScissorsHeight/3)

sizedScissors = scissors_img.resize((scissors_w,scissors_h))

Scissors_Pimage = PhotoImage(sizedScissors)

button_Scissors = tk.Button(fence, image=Scissors_Pimage, command=_scissors)
button_Scissors.place(x=350,y=0)

#score Table
label_Kira = tk.Label(text="Kira's Score:", font=("Montserrat", 25))
label_Kira.place(x=15, y=200)
label_User = tk.Label(text="User's Score:", font=("Montserrat", 25))
label_User.place(x=15, y=240)

Kira_Score = tk.Label(text="-", font=("Montserrat", 25))
Kira_Score.place(x=235, y=200)
User_Score = tk.Label(text="-", font=("Montserrat", 25))
User_Score.place(x=235, y=240)


tk.mainloop()