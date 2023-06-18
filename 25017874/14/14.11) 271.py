def ss(x, n):
	st = ''
	while x > 0:
		st += str(x % n)
		x = x // n
	return st[::-1]


ans = []
for x in range(1, 10000):
	if ss(x, 9).count('3') > 0 and len(ss(x, 9)) == 3:
		y = x * 3
		if len(ss(y, 9)) == 3:
			ans.append(x)
print(ss(max(ans) + min(ans), 9))
