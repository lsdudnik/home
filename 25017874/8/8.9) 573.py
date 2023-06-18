# 281
from itertools import *

def double(n):
	for i in range(1, len(n)):
		if n[i] == n[i - 1]:
			return False
	return True

def alternation(n):
	for i in range(1, len(n)):
		if int(n[i]) % 2 == int(n[i - 1]) % 2:
			return False
	return True

count6, count4 = 0, 0
for i in range(10 ** 5, 10 ** 6):
	num = [int(x) for x in str(i)]
	if alternation(str(i)) and len(num) == len(set(num)) :
		count6 += 1
for i in range(10 ** 3, 10 ** 4):
	if double(str(i)):
		count4 += 1
if count4 > count6:
	print(4, count4 - count6)
else:
	print(6, count6 - count4)

print(count6, count4)

