def cond(n):
	if n > 0 and str(n)[-1] == '9':
		return True
	return False


ans = []
num = [int(x) for x in open('2398')]
for i in range(2, len(num)):
	a, b, c = num[i - 2], num[i - 1], num[i]
	if not cond(a) and cond(b) and not cond(c):
		ans.append(a + b + c)
print(len(ans), max(ans))