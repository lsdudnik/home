import turtle
turtle.screensize(100_000, 100_000)
turtle.tracer(0)
turtle.goto(0, 0)
turtle.dot(5, 'red')
size = 20

turtle.penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        turtle.goto(x * size, y * size)
        turtle.dot(3, 'gray')


turtle.goto(0, 0)
turtle.left(90)
turtle.pendown()
turtle.dot(10, 'red')
turtle.color('red')
turtle.tracer(10)

for _ in range(12):
    for _ in range(3):
        turtle.forward(6 * size)
        turtle.left(120)
    turtle.right(120)

turtle.exitonclick()


