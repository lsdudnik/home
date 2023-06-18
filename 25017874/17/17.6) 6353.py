ans = []
num = [int(x) for x in open('6353')]
mx = max([x for x in num if x % 118 == 0 and str(x)[-1] != '8'])
for i in range(2, len(num)):
	a, b, c = num[i-2], num[i-1], num[i]
	if a % 118 == 0 or b % 118 == 0 or c % 118 == 0:
		if str(a)[-3:] == '118' or str(b)[-3:] == '118' or str(c)[-3:] == '118':
			if (a + b + c) > mx:
				ans.append(a + b + c)
print(len(ans), max(ans) ** 2)