import turtle
color = ['red','green']
t= turtle.Pen()
t.speed(1)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(color[x%2])
    t.width(x/10+1)
    t.forward(x)
    t.left(185)
