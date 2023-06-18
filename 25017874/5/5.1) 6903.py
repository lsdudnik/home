ans = []
for n in range(1, 100):
	n2 = bin(n)[2:]
	for _ in range(2):
		if n2.count('1') % 2 == 0:
			n2 = '11' + n2[2:] + '00'
		else:
			n2 = '10' + n2[2:] + '11'
	ans.append([int(n2, 2), n])
print(max(ans))