
from turtle import *
import colorsys
bgcolor('black')
speed(0)
h = 0.8
for i in range(130):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.004
    begin_fill()
    fd(i*1)
    lt(200)
    fd(i*1)
    rt(100)
    for j in range(2):
        rt(60)
    end_fill()
hideturtle()
