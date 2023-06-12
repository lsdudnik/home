from fnmatch import *


def sm(n):
	s, p = 0, 1
	for item in n:
		if int(item) % 2 != 0:
			s += int(item)
		else:
			p *= int(item)
	return s + p


fr = [x for x in open('24_3.txt').readline().split('XX') if len(x) > 0][1:-1]
ans = []
for item in fr:
	if item.isdigit() and fnmatch(item, '3????78??45'):
		ans.append([int(item), sm(item)])
ans.sort(reverse = True)
print(ans[0])