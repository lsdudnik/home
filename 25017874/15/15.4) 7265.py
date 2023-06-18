for a in range(1, 500):
	flag = 1
	for x in range(1, 500):
		flag *= ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 100)
		if not flag:
			break
	if flag:
		print(a)
		break