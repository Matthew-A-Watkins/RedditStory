import turtle


# screen bios
wn = turtle.Screen()
wn.setup(1250,800)
wn.bgpic("bgfr1.png")
wn.tracer(0)
trg = turtle.register_shape
# Character models
trg("note_item.gif")
trg("Down_Walking1.gif")
trg("Down_Walking2.gif")
trg("Down_Still.gif")
trg("Up_Still.gif")
trg("Up_Walking1.gif")
trg("Up_Walking2.gif")
trg("Left_Walking1.gif")
trg("Left_Walking2.gif")
trg("Left_Still.gif")
trg("Right_Still.gif")
trg("Right_Walking1.gif")
trg("Right_Walking2.gif")
trg("Rock.gif")

# note setup 1
note = turtle.Turtle()
note.hideturtle()
note.penup()
note.speed(100)
note.shape("note_item.gif")

rocks = []
ecount = 0
for i in range(5):
    rocks.append(turtle.Turtle())


x = -100
for rock in rocks:
    rock.hideturtle()
    rock.speed(100)
    rock.shape("Rock.gif")
    rock.penup()
    rock.goto(x,-255)
    x += 150



# character bios
player = turtle.Turtle()
player.hideturtle()
player.speed(100)
player.shape("Right_Still.gif")
player.penup()
player.setposition(0,-224.5)
player.showturtle()

# pen
pen = turtle.Turtle()
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(-500,320)
pen.pendown()
pen.write("Inventory: ", align='center', font=("Courier", 24, 'normal'))

# note setup 2
note.goto(player.xcor()- 360, -240)
note.showturtle()

# global def
directionR = 'still'
directionL = 'still'
playerspeed = 30
room = 1
isnote = 'no'
count = 0
bg = 1
notespeed = 1
lmove = 'ree'
lcount = 0

### functions

# simple move left (basic way for the player to move)
def smove_left():
    global directionL
    if directionL == '1':
        player.shape("Left_Walking1.gif")
        directionL = '2'
    elif directionL == '2':
        player.shape("Left_Walking2.gif")
        directionL = '1'
    else:
        player.shape("Left_Walking2.gif")
        directionL = '1'
# total move player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    global lmove
    global directionL
    global lcount
    global room
    lcount = 0
    lmove = 'left'
    if player.xcor() <= -600:
        if room == 1:
            player.setx(-600)
            player.shape("Left_Still.gif")
        if room == 2:
            player.setx(600)
            player.shape("Left_Still.gif")
            room = 1
    else:
        smove_left()
        player.setx(x)

# simple move right for the player basic way to move

def smove_right():
    global directionR
    if directionR == '1':
        player.shape("Right_Walking1.gif")
        directionR = '2'
    elif directionR == '2':
        player.shape("Right_Walking2.gif")
        directionR = '1'
    else:
        player.shape("Right_Walking2.gif")
        directionR = '1'

# complete move right for the player
def move_right():
    x = player.xcor()
    x += playerspeed
    global directionR
    global room
    global lmove
    global lcount
    lmove = 'right'
    lcount = 0
    if player.xcor() >= 600:
        if room == 2:
            player.setx(600)
            player.shape("Right_Still.gif")
        if room == 1:
            player.setx(-600)
            player.shape("Right_Still.gif")
            room = 2
    else:
        smove_right()
        player.setx(x)
wn.listen()

wn.onkey(move_left, 'a')
wn.onkey(move_right, 'd')

while True:
    # change background loop
    count += 1
    if count%10 == 0:
        if bg == 1:
            wn.bgpic("bgfr2.png")
            bg = 2
        else:
            wn.bgpic("bgfr1.png")
            bg = 1
    if lmove != 'ree':
        lcount += 1
        if lcount%20 == 0:
            if lmove == 'left':
                player.shape("Left_Still.gif")
            if lmove == 'right':
                player.shape("Right_Still.gif")
            lmove = 'ree'
    # note
    if room == 1:

        if isnote == 'yes':
            note.hideturtle()
        if isnote != 'yes':
            note.showturtle()
            y = note.ycor()
            y += notespeed
            note.goto(note.xcor(), y)
            if note.ycor() >= -220 or note.ycor() <= -255:
                notespeed *= -1
        if note.distance(player) < 60:
            note.hideturtle()
            isnote = 'yes'
            note.color("white")
            note.goto(pen.xcor()+150, pen.ycor())
            note.pendown()
            note.write("Torn Note", align='center', font=("courier", 24, 'normal'))
    if room == 2:
        note.hideturtle()
        for rock in rocks:
            rock.showturtle()
    if room != 2:
        for rock in rocks:
            rock.hideturtle()


    wn.update()