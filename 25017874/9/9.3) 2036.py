count = 0
for item in open('2036.txt'):
	s = sorted(list(map(int, item.split())))
	if sum(s) == 180 and max(s) < 90:
		count += 1
print(count)

# 1194
