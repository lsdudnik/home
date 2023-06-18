def f(cur, end):
	if cur == end:
		return 1
	elif cur < end:
		return 0
	else:
		return f(cur - 1, end) + f(cur // 2, end)


print(f(30, 9) * f(9, 1))
