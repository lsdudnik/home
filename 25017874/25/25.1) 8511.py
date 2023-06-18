from fnmatch import fnmatch
for x in range(253, 10 ** 8, 253):
	if fnmatch(str(x), '12??15*6'):
		print(x, x // 253)