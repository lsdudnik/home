from itertools import *


def f(x, y, z, w):
	return ((w <= y) <= (x == y)) or (not z)


for var in product([0, 1], repeat = 5):
	tab = [(var[0], 0, 1, 0), (0, var[1], var[2], 0), (var[3], 1, 1, var[4])]
	if len(tab) == len(set(tab)):
		for p in permutations('xywz'):
			if [f(**dict(zip(p, row))) for row in tab] == [0, 0, 0]:
				print(*p, sep = '')
