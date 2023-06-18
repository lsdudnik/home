def ss_rev(x, n):
	x = x[::-1]
	s = 0
	for i in range(len(x)):
		s += int(x[i]) * n ** i
	return s


for n in range(10, 100):
	if ss_rev('103', n) == ss_rev('97', n + 2):
		print(n)
