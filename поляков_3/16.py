from functools import lru_cache


@lru_cache(None)
def f(n):
	if n > 10_000:
		return n - 10_000
	else:
		return f(n + 1) + f(n + 2)


for x in range(10_000, 0, -1):
	f(x)

print(f(12345) * (f(10) - f(12)) // f(11) + f(10101))
