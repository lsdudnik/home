from math import sqrt
def divisors(n):
	d = set()
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			d.add(i)
			d.add(n // i)
	return d
ans = []
num = [int(x) for x in open('6059')]
for i in range(1, len(num)):
	a, b = num[i-1], num[i]
	if a % 2 == 0 and b % 2 == 0 and len(divisors(a)) > 0 and len(divisors(b)) > 0:
		if max(divisors(a) & divisors(b)) > 100:
			ans.append(abs(a - b))
print(len(ans), max(ans))
