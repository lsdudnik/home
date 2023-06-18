ans = []
for n in range(1, 1000):
	n2 = bin(n)[2:]
	if n % 2 == 0:
		n2 = '1' + n2 + '0'
	else:
		n2 = '11' + n2 + '11'
	if int(n2, 2) > 52:
		ans.append(int(n2, 2))
print(min(ans))