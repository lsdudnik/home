def f(cur, end):
	if cur == end:
		return 1
	elif cur > end or cur == 22:
		return 0
	else:
		return f(cur + 1, end) + f(cur + 3, end) + f(cur ** 2, end)


print(f(2, 17) * f(17, 25))