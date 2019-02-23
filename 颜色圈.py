import turtle
import random
turtle.colormode(255)
t=turtle.Pen()
for i in range(100):
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    x1=random.randint(-300,300)
    x2=random.randint(-300,300)
    banjing=random.randint(10,100)
    t.pencolor(r,b,g)
    t.up()
    t.setpos(x1,x2)
    t.down()
    t.dot(banjing)
