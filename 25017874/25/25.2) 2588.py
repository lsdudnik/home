from math import sqrt


def simple(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True


def divisors(n):
	d = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			d.add(i)
			d.add(n // i)
	return d


for i in range(190202, 190261, 2):
	ch = sorted([x for x in divisors(i) if x % 2 == 0])
	if len(ch) == 4:
		print(ch[-2:][::-1])
