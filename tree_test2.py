# https://pythoncircle.com/post/387/python-script-6-wishing-merry-christmas-using-python-turtle/
import time
from turtle import *
from random import randint
import playsound
from threading import Thread
import sys
import os
def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    # fill the above shape
    turtle.end_fill()
    # Reset the orientation of the turtle
    turtle.setheading(0)


def ball(trt, x, y, size=9, colour="red"):
    trt.penup()
    trt.setpos(x, y)
    trt.color(colour)
    trt.begin_fill()
    trt.pendown()
    trt.circle(size)
    trt.end_fill()

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        #base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)



def play_music():
    libraries_path = resource_path('source')
    print(libraries_path)
    while 1:
        print('sleep 1')
        time.sleep(1)
        try:
            mp3 = os.path.join(libraries_path, 'Christmas_For_Kids_-_We_Wish_You_A_Merry_Christmas_Song.mp3')
            playsound.playsound(mp3)
        except Exception:
            print('file not found')

def create_circle(turtle, x, y, radius, color):
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(x, y)
    oogway.pendown()
    oogway.begin_fill()
    oogway.circle(radius)
    oogway.end_fill()

def create_many_flower():
    my_turtle = oogway
    ball(my_turtle, 95, -5)
    ball(my_turtle, -110, -5)
    ball(my_turtle, 80, 40, size=7, colour="yellow")
    ball(my_turtle, -98, 40, size=7, colour="yellow")
    ball(my_turtle, 70, 70, size=5)
    ball(my_turtle, -93, 70, size=5)


if __name__ == '__main__':

    Thread(target=play_music).start()
    # play_music()
    BG_COLOR = "#0080ff"
    # "Yesterday is history, tomorrow is a mystery, but today is a gift. That is why it is called the present.”
    # 	                                                    — Oogway to Po under the peach tree, Kung Fu Panda
    oogway = Turtle()
    # set turtle speed
    oogway.speed(2)
    screen = oogway.getscreen()
    # set background color
    screen.bgcolor(BG_COLOR)
    # set tile of screen
    screen.title("Merry Christmas")
    # maximize the screen
    screen.setup(width=1.0, height=1.0)

    y = -100
    # create tree trunk
    create_rectangle(oogway, "red", -15, y-60, 30, 60)

    # create tree
    width = 240
    oogway.speed(10)
    while width > 10:
        width = width - 10
        height = 10
        x = 0 - width/2
        create_rectangle(oogway, "green", x, y, width, height)
        y = y + height

    # create a star a top of tree
    oogway.speed(1)
    oogway.penup()
    oogway.color('yellow')
    oogway.goto(-20, y+10)
    oogway.begin_fill()
    oogway.pendown()
    for i in range(5):
        oogway.forward(40)
        oogway.right(144)
    oogway.end_fill()
    create_many_flower()  #
    tree_height = y + 40

    # create moon in sky
    # create a full circle
    create_circle(oogway, 230, 180, 60, "white")
    # overlap with full circle of BG color to make a crescent shape
    create_circle(oogway, 220, 180, 60, BG_COLOR)

    # now add few stars in sky
    oogway.speed(10)
    number_of_stars = randint(20,30)
    # print(number_of_stars)
    for _ in range(0,number_of_stars):
        x_star = randint(-(screen.window_width()//2),screen.window_width()//2)
        y_star = randint(tree_height, screen.window_height()//2)
        size = randint(5,20)
        oogway.penup()
        oogway.color('white')
        oogway.goto(x_star, y_star)
        oogway.begin_fill()
        oogway.pendown()
        for i in range(5):
            oogway.forward(size)
            oogway.right(144)
        oogway.end_fill()

    # print greeting message
    oogway.speed(1)
    oogway.penup()
    msg1 = "老公送给臭宝贝的圣诞树 "
    msg2 = '愿我的宝贝永远开心快乐 '
    oogway.goto(0, -200)  # y is in minus because tree trunk was below x axis
    oogway.color("white")
    oogway.pendown()
    oogway.write(msg1, move=False, align="center", font=("Arial", 15, "bold"))
    oogway.penup()
    oogway.goto(0, -300)  # y is in minus because tree trunk was below x axis
    # oogway.color("white")
    oogway.pendown()
    time.sleep(2)
    # oogway.pendown()

    oogway.write(msg2, move=False, align="center", font=("Arial", 15, "bold"))

    oogway.hideturtle()
    screen.mainloop()
