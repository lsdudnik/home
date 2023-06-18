st = '1' + '0' * 55
while '1' in st:
	if '10' in st:
		st = st.replace('10', '001', 1)
	else:
		st = st.replace('1', '00', 1)
print(st.count('0'))