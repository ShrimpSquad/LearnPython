from turtle import Screen, Turtle
import tkinter as tk

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue", "aliceblue")

for i in range(10):
    timmy.forward(100)
    timmy.right(90)


screen = Screen()
screen.exitonclick()