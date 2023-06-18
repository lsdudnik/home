# 15120
ans = set()
from itertools import *
name = 'светлана'
def double(n):
	for i in range(1, len(n)):
		if n[i] == n[i - 1]:
			return False
	return True
comb = list(map(''.join, product('светлана', repeat = 8)))
for item in comb:
	if double(item):
		for x in item:
			if item.count(x) != name.count(x):
				break
		else:
			ans.add(item)
print(len(ans))