from turtle import *
from PIL import Image
import os

WIDTH = HEIGHT = 600

def start_new_line(x, y):
    up()
    goto(x, y)
    down()

def draw(x, y): 
    goto(x, y)

def save_image():
    hideturtle()
    canvas = screen.getcanvas()
    canvas.postscript(file="main.eps", width=WIDTH, height=HEIGHT)
    ps_image = Image.open("main.eps")
    ps_image.save("main.png")
    os.remove("main.eps")
    showturtle()

screen = Screen()
screen.setup(WIDTH, HEIGHT)

left(90)
speed(0)

screen.onclick(start_new_line)
ondrag(None)  # unload the memory usage to avoid lags
ondrag(draw)

# clicking the "s" key will save the image
screen.onkey(save_image, "s")
screen.listen()

# keep the program running until we close it
screen.mainloop()
