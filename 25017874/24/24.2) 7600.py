st = open('24_7600 (1).txt').readline().replace('Q', '*').replace('R', '*').replace('S', '*')
st = st.split('**')
max_line = max(st, key=len)
if max_line != st[0] and max_line != st[-1]:
	print(len(max_line) + 2)
else:
	print(len(max_line) + 1)
