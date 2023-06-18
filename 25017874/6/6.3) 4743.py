from turtle import *
size = 60

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
left(90)
pendown()
dot(10, 'red')
color('red')
tracer(10)


for _ in range(10):
	forward(15 * size)
	right(60)


exitonclick()
print(int(2 * 100 * (2 ** 0.5)))