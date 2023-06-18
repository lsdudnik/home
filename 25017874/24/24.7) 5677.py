st = open('24_5677.txt').readline()
mx, sub = 0, st[:2]
var = ['DAD', 'ADD', 'DDA']
for i in range(2, len(st)):
	if (sub[-2:] + st[i]) in var:
		sub += st[i]
	else:
		mx = max(mx, len(sub))
		sub = st[i - 1: i + 1]
else:
	mx = max(mx, len(sub))
print(mx)