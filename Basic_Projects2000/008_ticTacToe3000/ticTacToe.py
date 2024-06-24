import time
import turtle
import random
import x_and_o_codes as xo

#window
window = turtle.Screen()
window.title('Tic Tac Toe')
window.bgcolor('lightblue')
window.setup(width=450, height=450)
window.tracer(0)

#table
def table():
    ok = turtle.Turtle()
    ok.penup()
    ok.left(90)
    ok.forward(100)
    ok.left(-90)
    ok.back(150)
    ok.pendown()
    ok.forward(300)

    ok.penup()
    ok.left(-90)
    ok.forward(100)
    ok.left(-90)
    ok.pendown()
    ok.forward(300)

    ok.penup()
    ok.left(-90)
    ok.forward(200)
    ok.left(-90)
    ok.forward(100)
    ok.left(-90)
    ok.pendown()
    ok.forward(300)

    ok.penup()
    ok.left(90)
    ok.forward(100)
    ok.left(90)
    ok.pendown()
    ok.forward(300)

    ok.penup()
    ok.forward(3000000)


loc1 = turtle.Turtle()
loc1.speed(0)
loc1.shape("circle")
loc1.color("grey")
loc1.penup()
loc1.shapesize(0.80, 0.80)
loc1.goto(-100, 150)

loc2 = turtle.Turtle()
loc2.speed(0)
loc2.shape("circle")
loc2.color("grey")
loc2.penup()
loc2.shapesize(0.80, 0.80)
loc2.goto(0, 150)

loc3 = turtle.Turtle()
loc3.speed(0)
loc3.shape("circle")
loc3.color("grey")
loc3.penup()
loc3.shapesize(0.80, 0.80)
loc3.goto(100, 150)

loc4 = turtle.Turtle()
loc4.speed(0)
loc4.shape("circle")
loc4.color("grey")
loc4.penup()
loc4.shapesize(0.80, 0.80)
loc4.goto(-100, 50)

loc5 = turtle.Turtle()
loc5.speed(0)
loc5.shape("circle")
loc5.color("grey")
loc5.penup()
loc5.shapesize(0.80, 0.80)
loc5.goto(0, 50)

loc6 = turtle.Turtle()
loc6.speed(0)
loc6.shape("circle")
loc6.color("grey")
loc6.penup()
loc6.shapesize(0.80, 0.80)
loc6.goto(100, 50)

loc7 = turtle.Turtle()
loc7.speed(0)
loc7.shape("circle")
loc7.color("grey")
loc7.penup()
loc7.shapesize(0.80, 0.80)
loc7.goto(-100, -50)

loc8 = turtle.Turtle()
loc8.speed(0)
loc8.shape("circle")
loc8.color("grey")
loc8.penup()
loc8.shapesize(0.80, 0.80)
loc8.goto(0, -50)

loc9 = turtle.Turtle()
loc9.speed(0)
loc9.shape("circle")
loc9.color("grey")
loc9.penup()
loc9.shapesize(0.80, 0.80)
loc9.goto(100, -50)

location = 0

def clicked(x,y):
    if((x<=-50)and(x>=-150) and (y>=100)and(y<=200)):
        location = 1
    elif ((x>=-50)and(x<=50) and (y>=100)and(y<=200)):
        location = 2
    elif ((x>=50)and(x<=150) and (y>=100)and(y<=200)):
        location = 3
    elif((x<=-50)and(x>=-150) and (y>=0)and(y<=100)):
        location = 4
    elif ((x>=-50)and(x<=50) and (y>=0)and(y<=100)):
        location = 5
    elif ((x>=50)and(x<=150) and (y>=0)and(y<=100)):
        location = 6
    elif((x<=-50)and(x>=-150) and (y>=-100)and(y<=0)):
        location = 7
    elif ((x>=-50)and(x<=50) and (y >= -100) and (y <= 0)):
        location = 8
    elif ((x>=50)and(x<=150) and (y >= -100) and (y <= 0)):
        location = 9

turtle.onscreenclick(clicked)

move = 0
def game():
    if move == 0:
        location = random.randint(1, 9)
        if location == 1:
            xo.xloc1()
            print(location)
        elif location == 2:
            xo.xloc2()
            print(location)


game()
table()
while True:
    window.update()
