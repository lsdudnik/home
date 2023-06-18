from itertools import *
def couples(x):
	for n in permutations('0123', 2):
		s1 = x[int(n[1])] + x[int(n[0])]
		s2 = sum(x) - s1
		if s1 == s2:
			return True
	else:
		return False

count = 0
for item in open('6897'):
	s = sorted(list(map(int, item.split())))
	if s[-1] < sum(s[:-1]) and not couples(s):
		count += 1
print(count)

