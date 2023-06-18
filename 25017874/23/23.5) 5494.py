def f(cur, end, prev, last):
	if cur == end:
		return 1
	elif cur > end:
		return 0
	else:
		if last != prev:
			return f(cur + 1, end, last, 1) + f(cur * 2, end, last, 2)
		if last == prev and last == 1:
			return f(cur * 2, end, last, 2)
		if last == prev and last == 2:
			return f(cur + 1, end, last, 1)


print(f(1, 16, 0, -1))
