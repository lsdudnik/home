# 87

from itertools import *
count = 0
comb = list(map(''.join, product('abcde', repeat = 4)))
sg, gl = 'bcd', 'ae'
for item in comb:
	if item[-1] in sg and item[1] in 'abc' and item[0] != item[1]:
		if (item[0] in gl and item[2] in sg) or (item[0] in sg and item[2] in gl):
			count += 1
print(count)
