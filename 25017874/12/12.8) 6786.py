def simple(n):
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True
for n in range(1, 1000):
	st = '>' + '0' * 39 + '1' * n + '2' * 39
	while '>1' in st or '>2' in st or '>0' in st:
		st = st.replace('>1', '22>', 1)
		st = st.replace('>2', '2>', 1)
		st = st.replace('>0', '1>', 1)
	s = sum([int(x) for x in st if x != '>'])
	if simple(s):
		print(n)
		break
