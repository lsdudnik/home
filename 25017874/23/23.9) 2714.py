def f(cur, end, flag):
	if cur % 2 == 0:
		flag += 1
	if cur == end and flag == 6:
		return 1
	elif cur > end or flag > 6:
		return 0
	else:
		return f(cur + 1, end, flag) + f(cur + 3, end, flag) + f(cur + 5, end, flag)


print(f(3, 25, 0))