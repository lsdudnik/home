count = 0
def ss(n, x):
	st = ''
	while n > 0:
		st += str(n % x)
		n //= x
	return st[::-1]

for i in range(9 ** 6, 9 ** 7):
	if ss(i, 9).count('8') == 1:
		if int(ss(i, 9)[0]) % 2 == 0 and int(ss(i, 9)[-1]) % 2 != 0:
			count += 1
print(count)

# 376832