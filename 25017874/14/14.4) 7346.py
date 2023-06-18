def ss(x, n):
	x = x[::-1]
	s = 0
	for i in range(len(x)):
		s += int(x[i]) * n ** i
	return s
for x in range(67):
	s1 = ss('3021', 81) + x * 81 ** 2
	s2 = ss('1704', 67) + x * 67
	summ = s1 + s2
	if summ % 35 == 0:
		print(summ // 35)