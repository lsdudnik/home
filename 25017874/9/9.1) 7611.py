# 15058
count = 0
for item in open('7611.txt'):
	s = sorted(list(map(int, item.split())))
	if len(s) == len(set(s)) and (s[0] + s[-1]) * 2>= sum(s[1:-1]):
		count += 1
print(count)