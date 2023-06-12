from itertools import *

data = {'11', '0011', '101', '100', '0010', '0101', '0001', '0000', '011'}


def fano(x, have):
	for item in data:
		if len(x) < len(item):
			if item.startswith(x):
				return False
		elif len(x) >= len(item):
			if x.startswith(item):
				return False
	return True


for i in range(1, 6):
	comb = list(map(''.join, product('01', repeat = i)))
	for x in comb:
		if x not in data and fano(x, data):
			print(x)
