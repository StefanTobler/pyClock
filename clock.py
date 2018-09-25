import turtle
import time
width = 800
height = 800

turtle.setup(width, height)
turtle.bgpic("ClockFace.png")
turtle.mode("world")
turtle.title("Clock")

turtle.hideturtle()
turtle.speed(0)
turtle.up()
turtle.goto(0,-width * .45)
turtle.down()
turtle.width(4)
turtle.circle(width * .45)

second_hand = turtle.Turtle()
second_hand.pencolor(1, 0, 0)
second_hand.pensize(3)
second_hand.hideturtle()
second_hand.speed(0)
minute_hand = turtle.Turtle()
minute_hand.pensize(3)
minute_hand.hideturtle()
minute_hand.speed(0)
hour_hand = turtle.Turtle()
hour_hand.pensize(3)
hour_hand.hideturtle()
hour_hand.speed(0)

cast = time.localtime()
minutes = cast[4]
seconds = cast[5]
hours = cast[3]


second_hand.setheading(-(6 * seconds) + 90)
minute_hand.setheading(-(6 * minutes) + 90)
hour_hand.setheading(-(30 * hours + .5 * minutes) + 90)

# Initial Draw
second_hand.forward(width * .43)
minute_hand.forward(width * .37)
hour_hand.forward(width * .3)

def updateTime():
    global minutes, seconds, hours, second_hand, minute_hand
    second_hand.undo()
    seconds += 1
    if seconds > 59:
        seconds = 0
        minutes += 1
        minute_hand.undo()
        minute_hand.right(6)
        minute_hand.forward(width * .37)
        hour_hand.undo()
        hour_hand.right(.5)
        hour_hand.forward(width * .3)
    if minutes > 59:
        minutes = 0
        hours += 1
    if hours > 12:
        hours -= 12
    second_hand.right(6)
    second_hand.forward(width * .43)

while True:
    time.sleep(.955)
    updateTime()
    turtle.update()
