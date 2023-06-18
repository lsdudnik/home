from itertools import *

data = {'1010', '1100', '0'}


def fano(x, have):
	for item in data:
		if len(x) < len(item):
			if item.startswith(x):
				return False
		elif len(x) >= len(item):
			if x.startswith(item):
				return False
	return True

# 111


for i in range(1, 6):
	comb = list(map(''.join, product('01', repeat = i)))
	for x in comb:
		if x not in data and fano(x, data):
			print(x)
