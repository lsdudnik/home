data = open('5325.txt')
n = int, data.readline().split()
box = sorted(set([int(x) for x in data]))
ans = [] # максимум, сторона стартовой
for start in range(10):
	cur = box[start]
	count = 1
	i = 1
	while cur < max(box) and i < len(box):
		if box[i] - cur >= 3:
			cur = box[i]
			count += 1
		i += 1
	else:
		ans.append([count, box[start]])
# print(*sorted(ans, reverse = True), sep = '\n')
print(sorted(ans, reverse = True)[0])