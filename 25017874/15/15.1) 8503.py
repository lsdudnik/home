for a in range(500):
	flag = 1
	for x in range(500):
		flag *= ((x & 52 != 0) and (x & 36 == 0)) <= (x & a != 0)
		if not flag:
			break
	if flag:
		print(a)
		break