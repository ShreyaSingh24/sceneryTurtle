import turtle
import math
# setting the background color
a = turtle.Screen()
a.bgcolor("darkblue")
#creating the turtle and defining its speed
tk = turtle.Turtle()
tk.speed(180)
#define a function to make a rectangle
def drrec(t, width, height, color):
 t.fillcolor(color)
 t.begin_fill()
 t.forward(width)
 t.left(90)
 t.forward(height)
 t.left(90)
 t.forward(width)
 t.left(90)
 t.forward(height)
 t.left(90)
 t.end_fill()

#define a function to make a equilateral triangle
def drtri(t, length, color):
 t.fillcolor(color)
 t.begin_fill()
 t.forward(length)
 t.left(135)
 t.forward(length / math.sqrt(2))
 t.left(90)
 t.forward(length / math.sqrt(2))
 t.left(135)
 t.end_fill()
#define a function to draw a star
def drst(t,size,color):
 count = 0
 angle = 144
 t.fillcolor(color)
 t.begin_fill()
 for _ in range(5):
 t.forward(size)
 t.right(angle)
 t.end_fill()

#Tree trunk
tk.penup()
tk.goto(100, -200)
tk.pendown()
drrec(tk, 20, 110, "brown")
tk.penup()
tk.goto(250, -200)
tk.pendown()
drrec(tk, 20, 110, "brown")
tk.penup()
tk.goto(-140, -200)
tk.pendown()
drrec(tk, 20, 110, "brown")
tk.penup()
tk.goto(-290, -200)
tk.pendown()
drrec(tk, 20, 110, "brown")
#Tree top
tk.penup()
tk.goto(65, -90)
tk.pendown()
drtri(tk, 90, "lightgreen")
tk.penup()
tk.goto(70, -45)
tk.pendown()
drtri(tk, 80, "lightgreen")
tk.penup()
tk.goto(75, -5)
tk.pendown()
drtri(tk, 70, "lightgreen")
tk.penup()
tk.goto(80, 30)
tk.pendown()
drtri(tk, 70, "lightgreen")
tk.penup()
tk.goto(215, -90)
tk.pendown()
drtri(tk, 90, "lightgreen")
tk.penup() 
tk.goto(220, -45)
tk.pendown()
drtri(tk, 80, "lightgreen")
tk.penup()
tk.goto(225, -5)
tk.pendown()
drtri(tk, 70, "lightgreen")
tk.penup()
tk.goto(230, 30)
tk.pendown()
drtri(tk, 70, "lightgreen")
tk.penup()
tk.goto(-175, -90)
tk.pendown()
drtri(tk, 90, "lightgreen")
tk.penup()
tk.goto(-170, -45)
tk.pendown()
drtri(tk, 80, "lightgreen")
tk.penup()
tk.goto(-165, -5)
tk.pendown()
drtri(tk, 70, "lightgreen")
tk.penup()
tk.goto(-160, 30)
tk.pendown()
drtri(tk, 70, "lightgreen")
tk.penup()
tk.goto(-325, -90)
tk.pendown()
drtri(tk, 90, "lightgreen")
tk.penup()
tk.goto(-320, -45)
tk.pendown()
drtri(tk, 80, "lightgreen")
tk.penup()
tk.goto(-315, -5)
tk.pendown()
drtri(tk, 70, "lightgreen")
tk.penup()
tk.goto(-310, 30)
tk.pendown()
drtri(tk, 70, "lightgreen")
#front of the house
tk.penup()
tk.goto(-50, -200)
tk.pendown()
drrec(tk, 100, 110, "green")
#front door
tk.penup()
tk.goto(-20, -200)
tk.pendown()
drrec(tk, 40, 60, "yellow")
#window
tk.penup()
tk.goto(20, -130)
tk.pendown()
drrec(tk, 20, 30, "red")
tk.penup()
tk.goto(20, -115)
tk.pendown()
tk.forward(20)
tk.penup()
tk.goto(-40, -130)
tk.pendown()
drrec(tk, 20, 30, "red")
tk.penup()
tk.goto(-40, -115)
tk.pendown()
tk.forward(20)
#roof of the house
tk.penup()
tk.goto(-50, -90)
tk.pendown()
drtri(tk, 100, "black")
#moon
tk.penup()
tk.goto(200, 190)
tk.fillcolor("white")
tk.pendown()
tk.begin_fill()
tk.circle(45)
tk.end_fill()
#soil
tk.penup()
tk.goto(-340, -280)
tk.pendown()
drrec(tk, 720, 80, "brown")
#fencing
tk.penup()
tk.goto(50, -180)
tk.pendown()
drrec(tk, 290, 5, "white")
tk.penup()
tk.goto(-340, -180)
tk.pendown()
drrec(tk, 290, 5, "white")
tk.penup()
tk.goto(-100, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(-150, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(-200, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(-250, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(-300, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(100, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(150, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(200, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(250, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
tk.goto(300, -200)
tk.pendown()
drrec(tk, 5, 40, "white")
#stars
tk.penup()
tk.goto(0,240)
tk.pendown()
drst(tk, 12, "yellow")
tk.penup()
tk.goto(-130,240)
tk.pendown()
drst(tk, 15, "yellow")
tk.penup()
tk.goto(-80,230)
tk.pendown()
drst(tk, 12, "yellow")
tk.penup()
tk.goto(-220,200)
tk.pendown()
drst(tk, 12, "yellow")
tk.penup()
tk.goto(-190,170)
tk.pendown()
drst(tk, 12, "yellow")
tk.penup()
tk.goto(40,230)
tk.pendown()
drst(tk, 10, "yellow")
tk.penup() 
tk.goto(120,190)
tk.pendown()
drst(tk, 14, "yellow")
tk.penup()
tk.goto(220,170)
tk.pendown()
drst(tk, 10, "yellow")
tk.penup()
tk.goto(100,250)
tk.pendown()
drst(tk, 10, "yellow")
tk.penup()
tk.goto(-30,190)
tk.pendown()
drst(tk, 15, "yellow")
tk.penup()
tk.goto(-150,270)
tk.pendown()
drst(tk ,13, "yellow")
tk.penup()
tk.goto(-250,170)
tk.pendown()
drst(tk ,13, "yellow")
tk.penup()
tk.goto(-340,250)
tk.pendown()
drst(tk, 15, "yellow")
tk.penup()
tk.goto(280,250)
tk.pendown()
drst(tk, 15, "yellow")
tk.penup()
tk.goto(-300,190)
tk.pendown()
drst(tk, 15, "yellow")
tk.penup()
tk.goto(320,180)
tk.pendown()
drst(tk, 15, "yellow")
tk.penup()
tk.goto(-270,270)
tk.pendown()
drst(tk, 15, "yellow")