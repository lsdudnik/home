from fnmatch import fnmatch
count = 0
for line in open('634').readlines():
	if fnmatch(line, '*Z?RO*'):
		count += 1
print(count)