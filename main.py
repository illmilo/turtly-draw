from turtle import *

def start_new_line(x, y):
    up()
    goto(x, y)
    down()

def draw(x, y): 
    goto(x, y)

screen = Screen()
screen.setup(600, 600)

left(90)
speed(0)
screen.onclick(start_new_line)

ondrag(None)  # unload the memory usage to avoid lags
ondrag(draw)

# keep the program running until we close it
screen.mainloop()
