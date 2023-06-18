def ss(x, n):
	st = ''
	while x > 0:
		st += str(x % n)
		x = x // n
	return st[::-1]

ans = []
for n in range(96):
	if ss(n, 3)[-2:] == '21' and ss(n, 5)[0] == '3':
		ans.append(n)
print(sum(ans))