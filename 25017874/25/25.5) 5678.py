from fnmatch import fnmatch
for x in range(124579, 10 ** 8):
	if fnmatch(str(x), '124*5*79'):
		sm = sum([int(i) for i in str(x) if int(i) % 2 != 0])
		if x % sm == 0:
			print(x, sum([int(i) for i in str(x)]))