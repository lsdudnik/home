def game(h, st, fin):
	if h >= 55:
		return st % 2 == fin % 2
	elif st == fin:
		return 0
	else:
		next = [game(h + 1, st + 1, fin), game(h + 4, st + 1, fin), game(h * 3, st + 1, fin)]
		if (st + 1) % 2 == fin % 2:
			return any(next)
		else:
			return all(next)

ans = []
for s in range(1, 55):
	if game(s, 0, 2):
		ans.append([19, s])
	if game(s, 0, 3) and not game(s, 0, 1):
		ans.append([20, s])
	if game(s, 0, 4) and not game(s, 0, 2):
		ans.append([21, s])
print(*sorted(ans), sep='\n')