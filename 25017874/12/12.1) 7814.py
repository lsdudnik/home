for n in range(26, 1000):
	st = '2' + '4' * n
	while '14' in st or '244' in st or '444' in st:
		st = st.replace('14', '2', 1)
		st = st.replace('244', '14', 1)
		st = st.replace('444', '21', 1)
	suum = sum([int(x) for x in st])
	if suum > 20:
		print(n)
		break