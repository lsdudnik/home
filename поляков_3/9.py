count = 0
for item in open('9_3.txt'):
	line = sorted(list(map(int, item.split())))
	if len(line) == len(set(line)) and sum(line) / len(line) >= sum(line[2:4]) / 2:
		count += 1
print(count)

