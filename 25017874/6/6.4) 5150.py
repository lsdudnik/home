from turtle import *
size = 20

screensize(100_00, 100_00)
tracer(0)
goto(0, 0)
dot(5, 'red')


penup()
for x in range(-30, 30):
	for y in range(-30, 30):
		goto(x * size, y * size)
		dot(3, 'gray')

goto(0, 0)
pendown()
dot(10, 'red')
color('red')
tracer(10)


for _ in range(5):
	for _ in range(5):
		for _ in range(5):
			forward(2 * size)
			left(120)
		forward(2 * size)
		left(120)
		forward(2 * size)
	forward(2 * size)
	left(120)


exitonclick()
