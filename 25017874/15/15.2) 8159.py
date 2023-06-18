b = [x for x in range(50, 71)]
for a in range(1000):
	flag = 1
	for x in range(1000):
		for y in range(1000):
			flag *= (2 * x + y != 150) or (not (x  in b)) or (a > y)
		if not flag:
			break
	if flag:
		print(a)
		break

