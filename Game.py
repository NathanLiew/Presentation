import turtle
from turtle import *

s = turtle.getscreen()
t = turtle.Turtle()
t.pencolor("teal")
title("Etch-A-Sketch")


def movefd():
    t.fd(15)


def movert():
    t.rt(15)


def movelt():
    t.lt(15)


def movebk():
    t.bk(15)


def uraisemeup():
    t.penup()


def uletmedown():
    t.pendown()


def reset():
    t.reset()
    t.pencolor("teal")


def hideTurtle():
    t.hideturtle()


onkey(movebk, 's')
onkey(movefd, 'w')
onkey(movelt, 'a')
onkey(movert, 'd')
onkey(uraisemeup, 'e')
onkey(uletmedown, 'q')
onkey(reset, 'r')
onkey(hideturtle, 'h')

listen()
done()
