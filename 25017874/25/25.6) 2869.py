from math import sqrt
def divisors(n):
	d = set()
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			d.add(i)
			d.add(n // i)
	return d

count = 0
for i in range(460_000_000 + 1, 560_000_000):
	div = sorted(divisors(i), reverse = True)
	if len(div) > 5 and len(div) > 0:
		print(i, div[4])
		count += 1
	if count == 5:
		break