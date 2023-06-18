p = [x for x in range(10, 26)]
q = [x for x in range(15, 31)]
r = [x for x in range(20, 41)]
yet = []
for a in range(1, 100):
	flag = 0
	for x in range(1, 100):
		flag += ((x in q) <= (x not in r)) and (x == a) and (x not in p)
	if flag == 0:
		yet.append(a)
# print(yet)
for i in range(1, 100):
	if i in yet:
		print(i, end=" ")
	else:
		print('.', end=" ")