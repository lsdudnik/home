from itertools import *

data = {'1', '0000', '01'}


def fano(x, have):
	for item in data:
		if len(x) < len(item):
			if item.startswith(x):
				return False
		elif len(x) >= len(item):
			if x.startswith(item):
				return False
	return True


# 01 a
# 001 -
# 0001
# 0010
# 0011
print(4 + 2 + 1 + 2 + 4 + 2 + 4)
for i in range(1, 5):
	comb = list(map(''.join, product('01', repeat = i)))
	for x in comb:
		if x not in data and fano(x, data):
			print(x)
