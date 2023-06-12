floor1, floor2 = dict(), dict()
all_seats = {1, 2, 3, 4, 5, 6}

for item in open('26_3.txt'):
	item = list(map(int, item.split()))
	if item[0] == 1:
		if item[1] not in floor1:
			floor1[item[1]] = [item[2]]
		else:
			floor1[item[1]].append(item[2])
	else:
		if item[1] not in floor2:
			floor2[item[1]] = [item[2]]
		else:
			floor2[item[1]].append(item[2])

# floor1 = sorted(floor1.items(), reverse = False)
# floor2 = sorted(floor2.items(), reverse = False)
ans = []
for n_floor in [floor1, floor2]:
	for elem in n_floor:
		cur_no = elem
		cur_seats = set(n_floor[elem])
		free = list(all_seats - cur_seats)
		if free[:4] == [1, 2, 3, 4] or free[-4:] == [3, 4, 5, 6]:
			ans.append(cur_no)

print(max(ans), len(ans))

# 9996 5029
