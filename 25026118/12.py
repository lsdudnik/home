for n in range(1_500, 0, -1):
	st = '1' + '5' * n + '2' + '5' * n
	while '15' in st or '255' in st or '555' in st:
		st = st.replace('15', '2', 1)
		st = st.replace('255', '1', 1)
		st = st.replace('555', '12', 1)
	su = sum([int(x) for x in st])
	if len(str(su)) == 3:
		print(n, su)
		break

for n in range(1, 1500):
	st = '1' + '5' * n + '2' + '5' * n
	while '15' in st or '255' in st or '555' in st:
		st = st.replace('15', '2', 1)
		st = st.replace('255', '1', 1)
		st = st.replace('555', '12', 1)
	# сумма цифр числа (если число в строке)
	s = 0
	for item in st:
		s += int(item)
	if 99 < s < 1000: # если число трехзначное
		print(n, s)
