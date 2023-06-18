from math import sqrt
def divisors(n):
	d = set()
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			d.add(i)
			d.add(n // i)
	return d

count = 0
for i in range(350_300 + 1, 500_000):
	div = sum(divisors(i))
	if div % 13 == 0 and div != 0:
		print(i, div // 13)
		count += 1
	if count == 6:
		break
