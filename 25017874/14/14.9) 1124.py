def ss(x, n):
	st = ''
	while x > 0:
		st += str(x % n)
		x = x // n
	return st[::-1]
for x in range(1, 1000):
	ex = 27 ** 7 - 3 ** 11 + 36 - x
	dig = sum([int(i) for i in ss(ex, 3)])
	if dig == 22:
		print(x)
		break