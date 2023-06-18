from sys import *
setrecursionlimit(5000)

def f(n):
	if n == 1:
		return 1
	else:
		return n * f(n - 1) + 1

print(f(3303) / f(3300))

# или

f = [0, 1, 3]
for n in range(3, 3304):
	f.append(n * f[n - 1] + 1)
print(f[3303] / f[3300])

