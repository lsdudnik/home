from turtle import *
def move(dx, dy):
	p = pos()
	goto(p + (dx, dy))
size = 10

screensize(100_00, 100_00)
tracer(0)
goto(0, 0)
dot(5, 'red')

penup()
s = 70
for x in range(-s, s):
	for y in range(-s, s):
		goto(x * size, y * size)
		dot(3, 'gray')

goto(0, 0)
left(90)
pendown()
dot(10, 'red')
color('blue')
tracer(10)
b = 2
move(3 * size, -6 * size)
for _ in range(5):
	move(4 * size, b * size)
	move(6 * size, -6 * size)

dot(8, 'black')

pencolor('red')
move(-53 * size, 26 * size)

exitonclick()
