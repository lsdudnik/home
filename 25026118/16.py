from functools import lru_cache
@lru_cache(None)
def f(n):
	if n > 3456:
		return n + 1
	elif n <= 3456 and n % 3 == 0:
		return f(n + 1) + f(n + 2)
	else:
		return f(n + n % 3) + 2

for x in range(3456, 0, -1):
	f(x)

print(f(12) - f(17))

# print(f(17) + 10)