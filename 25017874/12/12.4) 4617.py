st = '9' * 84
while '33333' in st or '999' in st:
	st = st.replace('33333', '99', 1)
	st = st.replace('999', '3', 1)
print(st)