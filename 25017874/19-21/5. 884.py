def game(h1, h2, st, fin):
	if h1 + h2 >= 30:
		return st % 2 == fin % 2
	elif st == fin:
		return 0
	else:
		next = [game(h1 + 1, h2, st + 1, fin), game(h1 * 2, h2, st + 1, fin), game(h1, h2 + 1, st + 1, fin),
		        game(h1, h2 * 2, st + 1, fin)]
		if (st + 1) % 2 == fin % 2:
			return any(next)
		else:
			return all(next)


count19 = 0
for s1 in range(1, 30):
	for s2 in range(1, 30):
		if game(s1, s2, 0, 2) and s1 + s2 < 30:
			count19 += 1
print(f'19: {count19}')

ans = []
for s in range(1, 200):
	if game(6, s, 0, 3) and not game(6, s, 0, 1):
		ans.append(s)
print(f'20: {sorted(ans)}')

count21 = 0
for s1 in range(1, 30):
	for s2 in range(1, 30):
		if not game(s1, s2, 0, 2) and game(s1, s2, 0, 4) and s1 + s2 < 30:
			count21 += 1
print(count21)