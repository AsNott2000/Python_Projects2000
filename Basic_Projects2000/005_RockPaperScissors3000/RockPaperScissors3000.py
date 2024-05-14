import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image
import random
from tkinter import messagebox

fence = tk.Tk()
fence.geometry("518x300")
fence.resizable(width=False, height=False)

moves = [
    "rock",
    "paper",
    "scissors"
]

kira_score = 0
user_score = 0

def quit():
    fence.destroy()
def _rock():
    global kira_score
    global user_score
    moveKira = random.choice(moves)
    if moveKira == "rock":
        messagebox.showinfo("INFO", "TIE" + "\n\nKira's Move= " + moveKira)
    elif moveKira == "paper":
        messagebox.showinfo("INFO", "KIRA WON" + "\n\nKira's Move= " + moveKira)
        kira_score +=1
        Kira_Scoreboard.config(text=kira_score)
    else:
        messagebox.showinfo("INFO", "YOU WON" + "\n\nKira's Move= " + moveKira)
        user_score += 1
        User_Scoreboard.config(text=user_score)
    if user_score == 3:
        messagebox.showinfo("INFO", "Game Finished. You won this game bro!")
        quit()
    elif kira_score == 3:
        messagebox.showinfo("INFO", "Game Over. Kira won this game bro!")
        quit()


def _paper():
    global kira_score
    global user_score
    moveKira = random.choice(moves)
    if moveKira == "rock":
        messagebox.showinfo("INFO", "YOU WIN" + "\n\nKira's Move= " + moveKira)
        user_score += 1
        User_Scoreboard.config(text=user_score)
    elif moveKira == "paper":
        messagebox.showinfo("INFO", "TIE" + "\n\nKira's Move= " + moveKira)
    else:
        messagebox.showinfo("INFO", "KIRA WIN" + "\n\nKira's Move= " + moveKira)
        kira_score += 1
        Kira_Scoreboard.config(text=kira_score)
    if user_score == 3:
        messagebox.showinfo("INFO", "Game Finished. You won this game bro!")
        quit()
    elif kira_score == 3:
        messagebox.showinfo("INFO", "Game Over. Kira won this game bro!")
        quit()


def _scissors():
    global kira_score
    global user_score
    moveKira = random.choice(moves)
    if moveKira == "rock":
        messagebox.showinfo("INFO", "KIRA WON" + "\n\nKira's Move= " + moveKira)
        global kira_score
        kira_score += 1
        Kira_Scoreboard.config(text=kira_score)
    elif moveKira == "paper":
        messagebox.showinfo("INFO", "YOU WON" + "\n\nKira's Move= " + moveKira)
        global user_score
        user_score += 1
        User_Scoreboard.config(text=user_score)
    else:
        messagebox.showinfo("INFO", "TIE" + "\n\nKira's Move= " + moveKira)
    if user_score == 3:
        messagebox.showinfo("INFO", "Game Finished. You won this game bro!")
        quit()
    elif kira_score == 3:
        messagebox.showinfo("INFO", "Game Over. Kira won this game bro!")
        quit()


#Rock Button
rock_img = Image.open('./img/rock.png')
RockWidth, RockHeight = rock_img.size

rock_w = int(RockWidth / 3)
rock_h = int(RockHeight / 3)

sizedRock = rock_img.resize((rock_w, rock_h))

Rock_Pimage = PhotoImage(sizedRock)

button_Rock = tk.Button(fence, image=Rock_Pimage, command=_rock)
button_Rock.place(x=0, y=0)

#Paper Button
paper_img = Image.open('./img/paper.png')
PaperWidth, PaperHeight = paper_img.size

paper_w = int(PaperWidth / 3)
paper_h = int(PaperHeight / 3)

sizedPaper = paper_img.resize((paper_w, paper_h))

Paper_Pimage = PhotoImage(sizedPaper)

button_Paper = tk.Button(fence, image=Paper_Pimage, command=_paper)
button_Paper.place(x=175, y=0)

#Scissors Button
scissors_img = Image.open('./img/scissors.png')
ScissorsWidth, ScissorsHeight = scissors_img.size

scissors_w = int(ScissorsWidth / 3)
scissors_h = int(ScissorsHeight / 3)

sizedScissors = scissors_img.resize((scissors_w, scissors_h))

Scissors_Pimage = PhotoImage(sizedScissors)

button_Scissors = tk.Button(fence, image=Scissors_Pimage, command=_scissors)
button_Scissors.place(x=350, y=0)

#score Table
label_Kira = tk.Label(text="Kira's Score:", font=("Montserrat", 25))
label_Kira.place(x=15, y=200)
label_User = tk.Label(text="User's Score:", font=("Montserrat", 25))
label_User.place(x=15, y=240)

Kira_Scoreboard = tk.Label(text="0", font=("Montserrat", 25))
Kira_Scoreboard.place(x=235, y=200)
User_Scoreboard = tk.Label(text="0", font=("Montserrat", 25))
User_Scoreboard.place(x=235, y=240)


tk.mainloop()

