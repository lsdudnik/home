from itertools import *


def f(x, y, z, w):
	return (w and ((z or y) == (z and x)))


# var[]
for var in product([0, 1], repeat = 5):
	tab = [(1, var[0], 1, 0), (0, var[1], var[2], var[3]), (1, 1, 1, var[4])]
	if len(tab) == len(set(tab)):
		for p in permutations('xywz'):
			if [f(**dict(zip(p, row))) for row in tab] == [1, 1, 0]:
				print(*p, sep = '')

# print('x', 'y', 'z', 'w', 'F')
# for x in range(0, 2):
# 	for y in range(0, 2):
# 		for z in range(0, 2):
# 			for w in range(0, 2):
# 				F = w and ((z or y) == (z and x))
# 				# if F == 1:
# 				print(x, y, z, w, F)
