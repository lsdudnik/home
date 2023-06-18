from math import sqrt


def divisors(n):
	divisors = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			divisors.add(i)
			divisors.add(n // i)
	return divisors

ans, mx_div, digit = [], 0, 0
num = [int(x) for x in open('4329')]
for item in num:
	if len(divisors(item)) > mx_div:
		mx_div = len(divisors(item))
		digit = item

for i in range(1, len(num)):
	a, b = num[i - 1], num[i]
	if len(divisors(a) & divisors(digit)) >= 3 and len(divisors(b) & divisors(digit)) >= 3:
		ans.append(len((divisors(a) & divisors(b))))

print(len(ans), max(ans))
