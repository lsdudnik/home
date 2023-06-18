def ss(x, n):
	st = ''
	while x > 0:
		st += str(x % n)
		x = x // n
	return st[::-1]

for x in range(16):
	s1 = int('b7a' + hex(x)[2:] + '9', 16)
	s2 = int('54' + hex(x)[2:] + 'ed', 16)
	summ = ss(s1 + s2, 6)
	sum_dig = sum([int(x) for x in summ])
	if sum_dig == 25:
		print(s1 + s2)