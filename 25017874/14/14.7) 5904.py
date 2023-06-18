def ss_rev(x, n):
	x = x[::-1]
	s = 0
	for i in range(len(x)):
		s += int(x[i]) * n ** i
	return s

def ss(x, n):
	st = ''
	while x > 0:
		st += str(x % n)
		x = x // n
	return st[::-1]

ans = []
for x in range(20):
	for y in range(5):
		s1 = (4)  + (x * 20) + (3 * 20 ** 2) + (x * 20 ** 3) + (2 * 20 ** 4) + (x * 20 ** 5) + (1 * 20 ** 6) + (x * 20 ** 7)
		s2 = ss_rev('1' + str(y) + '2' + str(y) + '3' + str(y) + '4' + str(y), 5)
		s = s1 - s2
		summ = sum([int(x) for x in ss(s, 7)])
		ans.append(summ)
print(max(ans))

