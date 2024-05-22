import time
import turtle

#window
window = turtle.Screen()
window.title('Tic Tac Toe')
window.bgcolor('lightblue')
window.setup(width=500, height=500)
window.tracer(0)

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

while True:
    window.update()
