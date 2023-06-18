# 883
from itertools import product


def double(n):
	for i in range(1, len(n)):
		if n[i] == n[i - 1]:
			return False
	return True


let = sorted(set([x for x in 'степуха']))
# ['а', 'е', 'п', 'с', 'т', 'у', 'х'] 7
ans = set()
comb = list(map(''.join, product('степуха', repeat = 4)))
for item in comb[1000:]:
	if double(item):
		ans.add(item)

print(len(ans))
