def rs(x):
	su = 0
	x = x[::-1]
	for i in range(len(x)):
		su += int(x[i], 16) * 100 ** i
	return su

def ss(x, n):
	st = ''
	while x > 0:
		st += str(x % n)
		x //= n
	return st[::-1]

for x in range(100, -1, -1):
	s1 = rs('7a00123') + x * 100 ** 4
	s2 = rs('1ba640') + x
	s3 = rs('098012c') + x * 100 ** 6
	if (s1 - s2 + s3) % 21 == 0:
		print(ss(x, 6))
		break
