# 1800
from itertools import permutations
gl = 'оа'
def doubleg(n):
	for i in range(1, len(n)):
		if n[i] in gl and n[i - 1] in gl:
			return True
	return False
ans = set()

comb = list(map(''.join, permutations('соточка')))
for item in comb:
	if doubleg(item):
		ans.add(item)
print(len(ans))

