def ss(x, n):
	x = x[::-1]
	s = 0
	for i in range(len(x)):
		s += int(x[i]) * n ** i
	return s

for x in range(15):
	s1 = ss('99658029', 15) + x * 15 ** 2
	s2 = ss('1020023', 15) + x * 15 ** 3
	if (s1 + s2) % 14 == 0:
		print((s1 + s2) // 14)

