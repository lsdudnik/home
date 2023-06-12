b = [x for x in range(70, 81)]
count = 0
for a in range(1, 500):
	flag = 0
	for x in range(1, 500):
		flag += (x % 12 == 0) and (x in b) and (x % a != 0)
		if flag != 0:
			break
	if flag == 0:
		count += 1
print(count)