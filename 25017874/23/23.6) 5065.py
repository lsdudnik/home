def f(cur, end, flag):
	if '5' in str(cur):
		flag += 1
	if cur == end and flag == 0:
		return 1
	elif cur > end:
		return 0
	else:
		return f(cur + 1, end, flag) + f(cur * 2, end, flag)


print(f(1, 60, 0))