from itertools import *


def f(x, y, z, w):
	return ((x <= z) <= y) or (not w)


for var in product([0, 1], repeat = 7):
	tab = [(1, 0, var[0], var[1]), (var[2], 1, 0, var[3]), (0, var[4], var[5], var[6])]
	if len(tab) == len(set(tab)):
		for p in permutations('xywz'):
			if [f(**dict(zip(p, row))) for row in tab] == [0, 0, 0]:
				print(*p, sep = '')
