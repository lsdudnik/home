st = 'А' * 50 + 'Б' * 110 + 'В' * 100
while 'АБ' in st or 'ВА' in st or 'ВБ' in st:
	st = st.replace('ВА', 'АВ', 1)
	st = st.replace('АБ', 'БА', 1)
	st = st.replace('ВБ', 'БВ', 1)
print(st[42] + st[111] + st[252])