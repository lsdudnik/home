mall = dict()
ln, m = 2015, 3  # этажей, расстояние
max_floor, count = 0, 0  # этажи


def free(n):
	place = set()
	temp = [0] * (max(n) + 2)
	for item in n:
		temp[item] = item
	for i in range(0, len(temp) - m):
		now = temp[i: i + m + 1]
		if now.count(0) == 1:
			pos = now.index(0)
			place.add(pos + i)
	return sorted(place)


for item in open('5458.txt'):
	item = list(map(int, item.split()))
	if item[0] not in mall:
		mall[item[0]] = [item[1]]
	else:
		mall[item[0]].append(item[1])
for floor in mall:
	shops = sorted(mall[floor])
	if len(free(shops)) != 0:
		max_floor = max(floor, max_floor)
		count += len(free(shops))
print(count, max_floor)

# 16 1692
# print(*sorted(mall.items()), sep='\n')
