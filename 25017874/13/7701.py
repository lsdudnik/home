st = 'JH HGA GH BJ BG KB AKDECF DKE EC CFI IGH'
dic = {s[0]: s[1] for s in st.split(' ')}
def f(start, end):
	return sum(f(start + s, end) for s in dic[start[- 1]] if s not in start)

print(f('J', 'J'))