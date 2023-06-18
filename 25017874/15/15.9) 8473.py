p = [x for x in range(5, 138)]
# истина
tr = []
for a in range(1, 300):
	f = 1
	for x in range(1, 300):
		f *= ((x % 115 == 0) and (x % 5 != 0)) or ((a % x == 0) <= (a % 5 != 0) and (a not in p))
		if f == 0:
			break
	if f == 1:
		tr.append(a)

# ложь
fls = []
for a in range(1, 300):
	f = 0
	for x in range(1, 300):
		f += ((x % 115 == 0) and (x % 5 != 0)) or ((a % x == 0) <= (a % 5 != 0) and (a not in p))
		if f == 1:
			break
	if f == 0:
		fls.append(a)

for i in range(1, 300):
	if i in tr or i in fls:
		print('.', end='')
	else:
		print(i, end='')
