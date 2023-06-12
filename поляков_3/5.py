ans = []
for n in range(1, 1000):
	n2 = bin(n)[2:]
	if n2.count('1') % 2 == 0:
		n2 = '10' + n2[2:] + '0'
	else:
		n2 = '11' + n2[2:] + '1'
	if int(n2, 2) > 40:
		ans.append([n, int(n2, 2)])
print(sorted(ans))