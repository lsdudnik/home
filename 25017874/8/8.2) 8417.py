from itertools import *
comb = list(map(''.join, product('ярослав', repeat = 5)))
ans = set()
gl = 'яоа'
sg = 'рслв'
def doubleg(n):
	for i in range(1, len(n)):
		if n[i] in gl and n[i - 1] in gl:
			return False
	return True
def doubleall(n):
	for item in n:
		if n.count(item) > 1:
			return False
	return True

for item in comb:
	g, s = 0, 0
	for var in gl:
		g += item.count(var)
	for var in sg:
		s += item.count(var)
	if s > g and doubleg(item) and doubleall(item):
		ans.add(item)
print(len(ans))