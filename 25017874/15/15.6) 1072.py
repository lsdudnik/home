p = set(x for x in range(2, 31) if x % 2 == 0)
q = set(x for x in range(1, 32, 3))
yet = []
for a in range(1, 100):
	flag = 1
	for x in range(1, 100):
		flag *= ((x == a) <= (x in p)) and ((x in q) <= (x != a))
	if flag == 1:
		yet.append(a)

for i in range(1, 100):
	if i in yet:
		print(i, end=" ")
	else:
		print('.', end=" ")
