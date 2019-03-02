import turtle
t=turtle.Pen()
colors=["red","blue","green","yellow","pink","gray","purple"]
for i in range(7):
    t.pencolor(colors[i])
    t.dot(100-i*10)
t.pencolor("gray")
t.width(10)
t.right(90)
t.up()
t.forward(50)
t.down()
t.forward(100)
    


