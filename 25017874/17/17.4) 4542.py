ans = []
num = [int(x) for x in open('4542')]
mn, mx = min([x for x in num if x % 37 == 0]), max([x for x in num if x % 73 == 0])
for i in range(1, len(num)):
	a, b = num[i-1], num[i]
	if (mx < a < mn) ^ (mx < b < mn):
		ans.append(a + b)
print(len(ans), min(ans))