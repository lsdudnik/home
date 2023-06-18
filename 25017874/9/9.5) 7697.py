count = 0


def all18(x):
	for item in x:
		if item != 18:
			return False
	return True


for item in open('7697'):
	s = sorted(list(map(int, item.split())))
	if sum(s) % 18 == 0 or all18(s):
		count += 1
print(count)
