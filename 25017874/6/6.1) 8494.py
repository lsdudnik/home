from turtle import *
size = 30

screensize(100_0, 100_0)
tracer(0)
goto(0, 0)
dot(5, 'red')


penup()
for x in range(-30, 30):
	for y in range(-30, 30):
		goto(x * size, y * size)
		dot(3, 'gray')

goto(0, 0)
left(90)
pendown()
dot(10, 'red')
color('red')
tracer(10)

right(315)
for _ in range(7):
	forward(12 * size)
	right(45)
	forward(6 * size)
	right(135)

exitonclick()
