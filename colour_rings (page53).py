import turtle

from itertools import cycle
colors = cycle(['blue','yellow', 'pink', 'green', 'purple','white','red'])


def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+10, angle-20,shift-10)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(30,0,1)


