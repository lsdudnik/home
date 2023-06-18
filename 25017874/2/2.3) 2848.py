from itertools import *


def f(x, y, z, w):
	return ((not y) <= (z == w)) and ((z <= x) == w)


#  var[]
for var in product([0, 1], repeat = 2):
	tab = [(1, 1, 0, 1), (0, 1, 1, 1), (0, var[0], var[1], 0)]
	if len(tab) == len(set(tab)):
		for p in permutations('xywz'):
			if [f(**dict(zip(p, row))) for row in tab] == [1, 1, 1]:
				print(*p, sep = '')


