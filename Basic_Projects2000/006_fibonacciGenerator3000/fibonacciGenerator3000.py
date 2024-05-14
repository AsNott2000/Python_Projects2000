import math

n = int(input("enter the fibonacci number: "))

f = ((1+math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2**n * math.sqrt(5))

print(int(f))