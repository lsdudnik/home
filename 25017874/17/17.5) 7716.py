def parity(n):
	ch, nch = [], []
	n = [int(x) for x in str(n)]
	for item in n:
		if item % 2 == 0:
			ch.append(item)
		else:
			nch.append(item)
	return [ch, nch]

ans = []
num = [int(x) for x in open('7716')]
mx = max([x for x in num if len(parity(x)[1]) == len(str(x))])
for i in range(1, len(num)):
	a, b = num[i-1], num[i]
	if len(parity(a)[0]) == len(str(a)) or len(parity(b)[0]) == len(str(b)):
		if a + b > mx:
			ans.append(a + b)
print(len(ans), max(ans))
