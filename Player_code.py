import turtle
import pygame
from time import sleep

wn = turtle.Screen()
wn.title("Reddit Story Mode")
wn.bgcolor("black")
wn.setup(800,800)
turtle.register_shape("note_item.gif")
pygame.mixer.init()

# global definitions
level = 'starting room'
playerspeed = 40
isnote = 'no'

# room write
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 350)
pen.write("Room: {}".format(level), align="center", font=("Courier", 24, "normal"))

# inventory
inv = turtle.Turtle()
inv.hideturtle()
inv.color('red')
inv.penup()
inv.speed(10)
inv.setposition(250,280)
inv.pendown()
inv.write("Inventory: ", align="center", font=('comic sans', 24, "normal"))

# note
note = turtle.Turtle()
note.hideturtle()
note.penup()
note.speed(20)
note.color("light grey")
note.shape('note_item.gif')
note.goto(0, -300)
note.showturtle()

# character setup

player = turtle.Turtle()
player.hideturtle()
player.color("white")
player.penup()
player.turtlesize(3)
player.speed(20)
player.shape("square")
player.setposition(-340, 0)
player.showturtle()

# functions

def move_right():
    x = player.xcor()
    x += playerspeed
    if player.xcor() >= 340:
        player.setposition(-340, 0)
        global level
        pen.clear()
        if level == 'starting room':
            level = 'rock room'
        pen.write("Room: {}".format(level), align="center", font=("Courier", 24, "normal"))

    else:
        player.setx(x)

# u/meg4watts made this code

def move_left():
    x = player.xcor()
    x -= playerspeed
    global level
    if player.xcor() <= -340:
        if level == 'starting room':
            player.setx(-340)
        elif level == 'rock room':
            player.setx(340)
            level = 'starting room'
        pen.clear()
        pen.write("Room: {}".format(level), align="center", font=("Courier", 24, "normal"))
    else:
        player.setx(x)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if player.ycor() <= -320:
        player.sety(-320)
    else:
        player.sety(y)
def move_up():
    y = player.ycor()
    y += playerspeed
    if player.ycor() >= 320:
        player.sety(320)
    else:
        player.sety(y)
def isNote():
    if isnote == 'yes':
        x = player.xcor()
        y = player.ycor()
        player.goto(1000,1000)
        inv.hideturtle()
        note.hideturtle()
        pen.hideturtle()
        pen.clear()
        inv.clear()
        note.clear()
        wn.bgpic('Note.png')
        wn.update()
        sleep(5)
        wn.update()
        wn.bgpic('black.png')
        inv.write("Inventory: ", align="center", font=('comic sans', 24, "normal"))
        pen.write("Room: {}".format(level), align="center", font=("Courier", 24, "normal"))
        note.write("Note", align='center', font=('Courier', 24, 'normal'))
        player.setposition(x, y)


# keyboard bindings

wn.listen()

wn.onkey(move_right, "d")
wn.onkey(move_left, "a")
wn.onkey(move_down, "s")
wn.onkey(move_up, "w")
wn.onkey(isNote, "space")

while True:
    if level == 'starting room':
        if isnote == 'yes':
            note.hideturtle()
        else:
            note.showturtle()
        if player.distance(note) <= 30:
            note.hideturtle()
            note.penup()
            note.goto(inv.xcor(), inv.ycor()-40)
            note.color('red')
            note.write("Note", align='center', font=('Courier', 24, 'normal'))
            isnote = 'yes'
            note.goto(1000,1000)
    elif level != 'starting room':
        note.hideturtle()

    wn.update()