import random
x = 0
while x == 0:
    print("Information: Keep a count in your mind. I will try to guess. If the number I guess is large, write it DOWN, "
          "if it is small, write it UP. ıf correct, write CORRECT.")
    print("input the number (pls 0 and 100 between): ")
    num = int(input())
    if num > 0 and num <100:
        x = x+1
y = 0
RandomNumberUp = 1
RandomNumberDown = 100
while y == 0:
    random_number = random.randint(RandomNumberUp,RandomNumberDown)
    print(random_number)
    print("up, down or correct?")
    up_down_correct = input()
    if up_down_correct == "correct":
        print("I founded!")
        y = 1
    elif up_down_correct == "up":
        RandomNumberUp = random_number + 1
    elif up_down_correct == "down":
        RandomNumberDown = random_number - 1

