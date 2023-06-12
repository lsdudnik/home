from itertools import *


def f(x, y, z, w):
	return ((x == z) or (x != w)) and ((y <= x) or (not z))


for var in product([0, 1], repeat = 9):
	tab = [(1, var[0], 1, 1), (var[1], 1, var[2], 1), (var[3], 1, 1, 1), \
	       (1, var[4], 1, var[5]), (var[6], 1, var[7], var[8])]
	if len(tab) == len(set(tab)):
		for p in permutations('xywz'):
			if [f(**dict(zip(p, row))) for row in tab] == [0, 0, 0, 0, 0]:
				print(*p, sep = '')
