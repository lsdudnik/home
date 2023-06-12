num = [int(x) for x in open('17_3.txt')]
ans = []


def ch_nch(x):
	x = str(x)[::-1]
	ch = [int(x[i]) for i in range(len(x)) if i % 2 == 0]
	nch = [int(x[i]) for i in range(len(x)) if i % 2 != 0]
	if sum(ch) != 0 and sum(nch) % sum(ch) == 0:
		return True


for i in range(2, len(num)):
	temp = num[i - 2:i + 1]
	if ch_nch(temp[0]) and ch_nch(temp[1]) and ch_nch(temp[2]):
		ans.append(sum(temp))
print(len(ans), min(ans))
