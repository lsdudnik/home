from functools import lru_cache


@lru_cache(maxsize = None)
def f(n):
	if n == 0:
		return 0
	elif n > 0 and n % 2 == 0:
		return f(n // 2) - 1
	else:
		return 1 + f(n - 1)


count = 0
for n in range(1000):
	if f(n) == 0:
		count += 1
print(count)
