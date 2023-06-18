ans = []
for n in range(1, 1000):
	n2 = bin(n)[2:]
	for _ in range(3):
		s_dig = sum([int(x) for x in str(int(n2, 2))])
		if s_dig % 2 != 0:
			n2 += '1'
		else:
			n2 += '0'
	if int(n2, 2) > 2054:
		ans.append(int(n2, 2))
print(min(ans))