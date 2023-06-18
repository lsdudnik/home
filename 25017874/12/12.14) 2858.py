for x in range(30):
	for y in range(30):
		for z in range(30):
			st = '0' + '1' * x + '2' * y + '3' * z + '0'
			count = len(st)
			while '00' not in st:
				st = st.replace('01', '210', 1)
				st = st.replace('02', '3101', 1)
				st = st.replace('03', '2012', 1)
			if st.count('1') == 70 and st.count('2') == 56 and st.count('3') == 23:
				print(count)
				break
