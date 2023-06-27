import turtle

from itertools import cycle
colors = cycle(['blue','yellow', 'pink', 'green', 'purple','white','red'])


def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size+5)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30)


