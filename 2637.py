data = open('2637.txt')
conditions = list(map(int, data.readline().split()))
disk, user = conditions[0], conditions[1]
file = sorted([int(x) for x in data])
done, mx = [], 0
i = 0
while sum(done) + file[i] <= disk:
	done.append(file[i])
	file.pop(i)
free = disk - sum(done) + max(done)
for i in range(len(file)):
	if free >= file[i]:
		mx = file[i]
	else:
		print(len(done), mx)
		break
