from itertools import *

data = {'1', '10', '100', '1000'}
# 100 a 1000 k

def fano(x, have):
	for item in data:
		if len(x) < len(item):
			if item.endswith(x):
				return False
		elif len(x) >= len(item):
			if x.endswith(item):
				return False
	return True
# кабанов 6
for i in range(1, 6):
	comb = list(map(''.join, product('01', repeat = i)))
	for x in comb:
		if x not in data and fano(x, data):
			print(x)
print(4 + 3 + 1 + 3 + 5 + 5 + 2)