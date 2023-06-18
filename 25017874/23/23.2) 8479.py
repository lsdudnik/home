def f(cur, end):
	if cur == end:
		return 1
	elif cur > end or cur == 50:
		return 0
	else:
		return f(cur + 5, end) + f(cur + 4, end) + f(cur * 2, end)

print(f(2, 22) * f(22, 73) * f(73, 100))
