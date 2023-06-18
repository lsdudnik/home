count = 0
for item in open('5489'):
	s = sorted(list(map(int, item.split())))
	if len(s) == len(set(s)):
		ch = [x for x in s if x % 2 == 0]
		nch = [x for x in s if x % 2 != 0]
		if len(ch) > len(nch) and sum(ch) < sum(nch):
			count += 1
print(count)