import turtle 
pen = turtle.Pen()
pen.speed(15)
degree=  90
pen.pensize(15)
turtle.bgcolor("Black")
colors = ["Red","Yellow","Green","Blue"]

for star in range(8):
    pen.pencolor(colors[star%4])
    pen.left(degree/2)
    pen.fd(450)
    pen.left(degree)
turtle.mainloop()
