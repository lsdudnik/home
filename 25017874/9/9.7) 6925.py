from statistics import *
# mean - среднее арифметическое
count = 0
for item in open('6925'):
	s = sorted(list(map(int, item.split())))
	ch = [x for x in s if x % 2 == 0]
	if len(ch) == 0:
		ch = [0]
	nch = [x for x in s if x % 2 != 0]
	if len(nch) == 0:
		nch = [0]
	if (abs(mean(ch) - mean(nch)) > 50) ^ (len(set(s)) == 5):
		count += 1
print(count)

