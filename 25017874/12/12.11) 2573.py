ans = []
for n in range(301, 1000):
	st = '5' * n
	while '55555' in st:
		st = st.replace('55555', '88', 1)
		st = st.replace('888', '55', 1)
	ans.append([st.count('5'), n])

for x in sorted(ans, reverse = True):
	if x[0] == max(sorted(ans, reverse = True))[0]:
		print(x)

