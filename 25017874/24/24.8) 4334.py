st = open('24_4334.txt').readline().split('A')
mx = 0
for i in range(4, len(st)):
	temp = ''.join(st[i - 4:i])
	if temp.count('R') >= 2:
		mx = max(mx, len(temp) + 3)
else:
	if temp.count('R') >= 2:
		mx = max(mx, len(temp) + 3)
print(mx)

