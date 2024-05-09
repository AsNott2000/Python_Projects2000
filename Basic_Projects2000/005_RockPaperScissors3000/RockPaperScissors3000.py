import random
import tkinter as tk
import time

def theGame():


    score_kira = 0
    score_user = 0
    print("Kira's Score: ", score_kira)
    print("Your Score: ", score_user)
    print("_____________")
    while score_user < 3 and score_kira < 3:
        moves = [
            "rock",
            "paper",
            "scissors"
        ]
        moveKira = random.choice(moves)
        moveInput = input("rock, paper or scissor? ").lower()
        print("Kira's Choices: ", moveKira)
        if moveInput == moveKira:
            print("tie")
        elif moveInput == "rock":
            if moveKira == "paper":
                print("Kira Won")
                score_kira += 1
            elif moveKira == "scissors":
                print("You Won")
                score_user += 1
        elif moveInput == "paper":
            if moveKira == "scissors":
                print("Kira Won")
                score_kira += 1
            elif moveKira == "rock":
                print("You Won")
                score_user += 1
        elif moveInput == "scissors":
            if moveKira == "rock":
                print("Kira Won")
                score_kira += 1
            elif moveKira == "paper":
                print("You Won")
                score_user += 1


        print("Kira's Score: ", score_kira)
        print("Your Score: ", score_user)
        print("_____________")

print("Hello my Friendoo! Watashi wa Kira Yoshikage")
time.sleep(1)
print("I'm 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married.")
time.sleep(1)
print("I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest.")
time.sleep(1)
print("Now we gonna play ROCK, PAPER, SCISSORS!")
time.sleep(1)
print("Be careful because you have 3 attempts. If you wanna win game, you defeat me 3 times!")
time.sleep(1)
print("Lets Play!!")

theGame()