from math import sqrt
def divisors(n):
	d = set()
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			d.add(i)
			d.add(n // i)
	return d


count = 0
for i in range(39_345_679, 0, -1):
	div = sorted(divisors(i))
	if 2 in div and 3 in div and 5 in div and 7 in div:
		if 76 <= len(div) <= 88:
			print(i, len(div))
			count += 1
	if count == 10:
		break