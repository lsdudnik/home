from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
	if n <= 4:
		return 1
	else:
		return f(n - 1) + f(n - 3) + g(n - 2)

@lru_cache(maxsize=None)
def g(n):
	if n > 1500:
		return 5
	else:
		return g(n + 1) + g(n + 2) + 1

for i in range(1500, 0, -1):
	g(i)
for i in range(1201):
	f(i)

print((f(1200) + g(100)) % 10_000)


