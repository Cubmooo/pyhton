import turtle
colours=['red','purple','blue']
gh=turtle
turtle.bgcolor('black')
gh.speed(15)
for x in range(10000000):
    gh.pencolor(colours[x%3])
    gh.width(x//100+1)
    gh.forward(x)
    gh.left(119)
    
    
turtle.exitonclick()