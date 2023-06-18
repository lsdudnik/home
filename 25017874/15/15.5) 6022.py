for a in range(500):
	flag = 1
	for x in range(500):
		for y in range(500):
			flag *= (x < a) or (y < a) or (x + 2 * y > 150)
			if not flag:
				break
	if flag:
		print(a)
		break
