count = 0
def ss(x, n):
	st = ''
	while x > 0:
		st += str(x % n)
		x //= n
	return st[::-1]

for x in range(7 ** 5, 7 ** 6):
	if int(ss(x, 7)[-1]) >= 4:
		ch, nch = 0, 0
		for item in ss(x, 7):
			if int(item) % 2 == 0:
				ch += 1
			else:
				nch += 1
		if ch == nch:
			count += 1
print(count)