for n in range(2000, 5, -1):
	st = '1' + '5' * n + '2' + '5' * n
	while '15' in st or '255' in st or '555' in st:
		st = st.replace('15', '2', 1)
		st = st.replace('255', '1', 1)
		st = st.replace('555', '12', 1)
	suum = sum([int(x) for x in st])
	if len(str(suum)) == 3:
		print(n)
		break
