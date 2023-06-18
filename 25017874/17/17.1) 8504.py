num = [int(x) for x in open('8504')]
mi = min([x for x in num if len(str(x)) == 3 and str(x)[-1] == '5'])
ans = []
for i in range(1, len(num)):
	if len(str(num[i])) == 3 or len(str(num[i - 1])) == 3:
		if (num[i] + num[i - 1]) % mi == 0:
			ans.append(num[i] + num[i - 1])

print(len(ans), max(ans))
