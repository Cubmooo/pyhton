import turtle
loadWindon= turtle.Screen()
turtle.speed(15)
i=0

while True:
    i=i+1
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)