from math import sqrt
def divisors(n):
	d = set()
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			d.add(i)
			d.add(n // i)
	return d

count = 0
for i in range(452_021 + 1, 600_000):
	div = divisors(i)
	if len(div) != 0:
		m = max(div) + min(div)
		if m % 7 == 3:
			count += 1
			print(i, m)
	if count == 5:
		break