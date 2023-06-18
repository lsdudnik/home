from itertools import *

# st =  '2' * 4 + '1' * 12
# st =  '1' * 12 + '2' * 4
st = '112' * 4 + '1' * 4
# all = list(map(''.join, permutations('1111111111112222')))
# for st in all:
while '11' in st:
	if '112' in st:
		st = st.replace('112', '7', 1)
	else:
		st = st.replace('11', '3', 1)
print(sum([int(x) for x in st]))
