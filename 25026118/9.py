count = 0
for item in open('9.txt'):
	st = sorted(list(map(int, item.split())))
	if (len(st) == len(set(st))) ^ ((st[-1] + st[0]) * 2 < sum(st[1:-1])):
		# if (len(st) == len(set(st))) + ((st[-1] + st[0]) * 2 < sum(st[1:-1])) == 1:
		count += 1
print(count)
