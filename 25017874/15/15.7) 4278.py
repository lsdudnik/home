count = 0
for a in range(1, 1000):
	flag = 1
	for x in range(1, 1000):
		flag *= (a % 12 == 0) and (530 % x == 0) <= ((a % x != 0) <= (170 % x != 0))
		if not flag:
			break
	if flag:
		count += 1
print(count)