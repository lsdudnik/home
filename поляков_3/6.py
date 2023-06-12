import turtle
turtle.screensize(1000, 1000)
turtle.tracer(0)
turtle.goto(0, 0)
turtle.dot(5, 'red')
size = 20

turtle.penup()
for x in range(-70, 70):
    for y in range(-70, 70):
        turtle.goto(x * size, y * size)
        turtle.dot(3, 'gray')


turtle.goto(0, 0)
turtle.left(90)
turtle.pendown()
turtle.dot(10, 'red')
turtle.color('red')
turtle.tracer(10)

for _ in range(15):
    turtle.forward(15 * size)
    turtle.right(120)

turtle.exitonclick()


