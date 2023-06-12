def f(cur, end, flag):
	if sum([int(x) for x in str(cur)]) == 14:
		flag += 1
	if cur == end and flag == 5:
		return 1
	elif cur > end:
		return 0
	else:
		return f(cur + 2, end, flag) + f(cur * 3, end, flag) + f(cur * 4, end, flag)


print(f(1, 600, 0))
