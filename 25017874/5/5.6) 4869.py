def count1(n):
	cur_count = 0
	for i in range(1, len(n), 2):
		if n[i] == '1':
			cur_count += 1
	return cur_count


def count0(n):
	cur_count = 0
	for i in range(0, len(n), 2):
		if n[i] == '0':
			cur_count += 1
	return cur_count


for n in range(1, 10000):
	n2 = bin(n)[2:]
	r = abs(count1(n2) - count0(n2))
	if r == 5:
		print(n)
		break
