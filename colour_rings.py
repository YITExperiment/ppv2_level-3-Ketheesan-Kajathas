import turtle

from itertools import cycle
colors = cycle(['blue', 'black', 'yellow', 'pink', 'green', 'purple','white','red'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle-20,shift+1)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(10)
draw_circle(30,0,1)


