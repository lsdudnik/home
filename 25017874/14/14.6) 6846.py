def ss(x, n):
	x = x[::-1]
	s = 0
	for i in range(len(x)):
		s += int(x[i]) * n ** i
	return s

for x in range(98):
	s1 = ss('12045', 98) + x * 98 ** 2
	s2 = ss('1098', 123) + x * 123 ** 2
	s = s1 + s2
	if s % 123 == 0:
		print(s // 123)