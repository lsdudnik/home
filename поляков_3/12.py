for k in range(1000):
	st = '>' + '1' * 22 + '2' * k + '3' * 23
	while '>1' in st or '>2' in st or '>3' in st:
		st = st.replace('>1', '2>', 1)
		st = st.replace('>2', '21>', 1)
		st = st.replace('>3', '11>', 1)
	s = sum([int(x) for x in st if x != '>'])
	if s > 2023:
		print(k)
		break
