def game(h, st, fin):
	if h >= 129:
		return st % 2 == fin % 2
	if st == fin:
		return 0
	else:
		next = [game(h + 1, st + 1, fin), game(h * 2, st + 1, fin)]
		if (st + 1) % 2 == fin % 2:
			return any(next)
		else:
			return all(next)
			#  return any(next)

# 19
for s in range(1, 129):
	if game(s, 0, 2):
		print(f'19: {s}')

# 20
p1, p2 = set(), set()
for s in range(1, 129):
	if game(s, 0, 1):
		p1.add(s)
	if game(s, 0, 3):
		p2.add(s)
print(f'20: {sorted(p2 - p1)}')

# 21
v1, v2 = set(), set()
for s in range(1, 129):
	if game(s, 0, 2):
		v1.add(s)
	if game(s, 0, 4):
		v2.add(s)
print(f'21: {min(v2 - v1)}')