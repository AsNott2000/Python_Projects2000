import random
x = 0
while x == 0:
    print("input the number (pls 0 and 100 between): ")
    num = int(input())
    if num > 0 and num <100:
        x = x+1
y = 0
RandomNumberYukari = 1
RandomNumberAsagi = 100
while y == 0:
    random_number = random.randint(RandomNumberYukari,RandomNumberAsagi)
    print(random_number)
    print("asagi mi yukari mi dogru mu")
    asagi_yukari_dogru = input()
    if asagi_yukari_dogru == "dogru":
        print("dogru buldum")
        y=1
    elif asagi_yukari_dogru == "yukari":
        RandomNumberYukari = random_number + 1
    elif asagi_yukari_dogru == "asagi":
        RandomNumberAsagi = random_number - 1

