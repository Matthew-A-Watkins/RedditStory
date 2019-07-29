import turtle
import pygame
from time import sleep

wn = turtle.Screen()
wn.title("Reddit Story Mode")
wn.bgcolor("black")
wn.setup(800,800)
pygame.mixer.init()

# global definitions
level = 'starting room'
playerspeed = 40
isnote = 'no'
FoundKey = False
FoundSKey = False
isDirectionR = 'Right_Still'
isDirectionL = 'Left_Still'
isDirectionU = 'Up_Still'
isDirectionD = 'Down_Still'


# Character models
turtle.register_shape("note_item.gif")
turtle.register_shape("Down_Walking1.gif")
turtle.register_shape("Down_Walking2.gif")
turtle.register_shape("Down_Still.gif")
turtle.register_shape("Up_Still.gif")
turtle.register_shape("Up_Walking1.gif")
turtle.register_shape("Up_Walking2.gif")
turtle.register_shape("Left_Walking1.gif")
turtle.register_shape("Left_Walking2.gif")
turtle.register_shape("Left_Still.gif")
turtle.register_shape("Right_Still.gif")
turtle.register_shape("Right_Walking1.gif")
turtle.register_shape("Right_Walking2.gif")
turtle.register_shape("Rock.gif")

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
inv.setposition(250,310)
inv.pendown()
inv.write("Inventory: ", align="center", font=('comic sans', 24, "normal"))

# note
note = turtle.Turtle()
note.hideturtle()
note.penup()
note.speed(20)
note.shape('note_item.gif')
note.goto(0, -300)
note.showturtle()

# rock
rock1 = turtle.Turtle()
rock1.hideturtle()
rock1.penup()
rock1.shape("Rock.gif")
rock1.speed(80)
rock1.goto(200,150)
rock1.setheading(90)


rock2 = turtle.Turtle()
rock2.hideturtle()
rock2.penup()
rock2.shape("Rock.gif")
rock2.speed(80)
rock2.goto(50,150)
rock2.setheading(90)


rock3 = turtle.Turtle()
rock3.hideturtle()
rock3.penup()
rock3.shape("Rock.gif")
rock3.speed(80)
rock3.goto(-100,150)
rock3.setheading(90)

rock4 = turtle.Turtle()
rock4.hideturtle()
rock4.penup()
rock4.shape("Rock.gif")
rock4.speed(80)
rock4.goto(-100,-150)
rock4.setheading(90)

rock5 = turtle.Turtle()
rock5.hideturtle()
rock5.penup()
rock5.shape("Rock.gif")
rock5.speed(80)
rock5.goto(50,-150)
rock5.setheading(90)

rock6 = turtle.Turtle()
rock6.hideturtle()
rock6.penup()
rock6.shape("Rock.gif")
rock6.speed(80)
rock6.goto(200,-150)
rock6.setheading(90)

rock1.goto(200,150)
rock2.goto(50,150)
rock3.goto(-100,150)
rock4.goto(-100,-150)
rock5.goto(50,-150)
rock6.goto(200,-150)
# character setup

player = turtle.Turtle()
player.hideturtle()
player.color("white")
player.penup()
player.turtlesize(3)
player.speed(20)
player.shape("Right_Still.gif")
player.setposition(-340, 0)
player.showturtle()

# Bronze key
Bkey = turtle.Turtle()
Bkey.hideturtle()
Bkey.color("red")
Bkey.penup()
Bkey.shape("square")
Bkey.goto(inv.xcor(), inv.ycor()-80)
Bkey.pendown()

SKey = turtle.Turtle()
SKey.hideturtle()
SKey.color("red")
SKey.penup()
SKey.shape("square")
SKey.goto(inv.xcor(), inv.ycor()-120)
SKey.pendown()

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
        player.shape("Right_Still.gif")

    else:
        global isDirectionR
        if isDirectionR == '1':
            player.shape("Right_Walking2.gif")
            isDirectionR = '2'
        elif isDirectionR == '2':
            player.shape("Right_Walking1.gif")
            isDirectionR = '1'
        else:
            player.shape("Right_Walking1.gif")
            isDirectionR = '1'
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
        player.shape("Left_Still.gif")
    else:
        global isDirectionL
        if isDirectionL == '1':
            player.shape("Left_Walking2.gif")
            isDirectionL = '2'
        elif isDirectionL == '2':
            player.shape("Left_Walking1.gif")
            isDirectionL = '1'
        else:
            player.shape("Left_Walking1.gif")
            isDirectionL = '1'

        player.setx(x)


def move_down():
    y = player.ycor()
    y -= playerspeed
    global level
    if player.ycor() <= -300:
        if level != 'scary hallway':
            player.sety(-300)
        if level == 'scary hallway':
            level = 'rock room'
            pen.clear()
            pen.write("Room: {}".format(level), align="center", font=("Courier", 24, "normal"))
            player.sety(320)
        player.shape("Down_Still.gif")

    else:
        global isDirectionD
        if isDirectionD == '1':
            player.shape("Down_Walking2.gif")
            isDirectionD = '2'
        elif isDirectionD == '2':
            player.shape("Down_Walking1.gif")
            isDirectionD = '1'
        else:
            player.shape("Down_Walking1.gif")
            isDirectionD = '1'
        player.sety(y)
def move_up():
    y = player.ycor()
    y += playerspeed
    if player.ycor() >= 320:
        global level
        if level =='rock room' and FoundKey == True:
            player.sety(-300)
            level = 'scary hallway'
            pen.clear()
            pen.write("Room: {}".format(level), align="center", font=("Courier", 24, "normal"))
        elif level == 'starting room':
            player.sety(320)
        player.shape("Up_Still.gif")
    else:
        global isDirectionU
        if isDirectionU == '1':
            player.shape("Up_Walking2.gif")
            isDirectionU = '2'
        elif isDirectionU == '2':
            player.shape("Up_Walking1.gif")
            isDirectionU = '1'
        else:
            player.shape("Up_Walking1.gif")
            isDirectionU = '1'
        player.sety(y)
def isNote():
    if isnote == 'yes':
        x = player.xcor()
        y = player.ycor()
        player.goto(1000,1000)
        inv.hideturtle()
        note.hideturtle()
        pen.hideturtle()
        rock1.hideturtle()
        rock2.hideturtle()
        rock3.hideturtle()
        rock4.hideturtle()
        rock5.hideturtle()
        rock6.hideturtle()
        pen.clear()
        Bkey.clear()
        inv.clear()
        note.clear()
        wn.bgpic('Note.png')
        wn.update()
        sleep(5)
        wn.bgpic('black.png')
        inv.write("Inventory: ", align="center", font=('comic sans', 24, "normal"))
        pen.write("Room: {}".format(level), align="center", font=("Courier", 24, "normal"))
        note.goto(inv.xcor(), inv.ycor() - 40)
        if FoundKey == True:
            Bkey.write("Bronze Key", align='center', font=('Courier', 24, 'normal'))
        note.write("Note", align='center', font=('Courier', 24, 'normal'))
        player.setposition(x, y)

def searchRock():
    if rock5.distance(player) < 40:
        global FoundKey
        FoundKey = True
    if rock1.distance(player) < 40:
        global FoundSKey
        FoundSKey = True

# keyboard bindings

wn.listen()

wn.onkey(move_right, "d")
wn.onkey(move_left, "a")
wn.onkey(move_down, "s")
wn.onkey(move_up, "w")
wn.onkey(isNote, "q")
wn.onkey(searchRock, "space")

while True:
    # note appearing and disappearing as well as going to inventory
    if level == 'starting room':
        if isnote == 'yes':
            note.hideturtle()
        else:
            note.showturtle()
        if player.distance(note) <= 50:
            note.hideturtle()
            note.penup()
            note.goto(inv.xcor(), inv.ycor()-40)
            note.color('red')
            note.write("Note", align='center', font=('Courier', 24, 'normal'))
            isnote = 'yes'
            note.goto(1000,1000)
    elif level != 'starting room':
        note.hideturtle()
    # rocks
    if level == 'rock room':
        rock1.goto(200,150)
        rock1.showturtle()
        rock2.showturtle()
        rock3.showturtle()
        rock4.showturtle()
        rock5.goto(50,-150)
        rock5.showturtle()
        rock6.showturtle()

    else:
        rock1.goto(1000,1000)
        rock1.hideturtle()
        rock2.hideturtle()
        rock3.hideturtle()
        rock4.hideturtle()
        rock5.goto(1000,1000)
        rock5.hideturtle()
        rock6.hideturtle()
    if FoundKey == True:
        Bkey.write("Bronze Key", align='center', font=('Courier', 24, 'normal'))
    if FoundSKey == True:
        SKey.write("Silver Key", align='center', font=('Courier', 24, 'normal'))


    wn.update()