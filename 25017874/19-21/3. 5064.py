def game(h, st, fin):
	if h >= 151:
		return st % 2 == fin % 2
	elif st == fin:
		return 0
	else:
		next = []
		if (h + 1) % 3 != 0:
			next.append(game(h + 1, st + 1, fin))
		if (h + 2) % 3!= 0:
			next.append(game(h + 2, st + 1, fin))
		if (h * 2) % 3!= 0:
			next.append(game(h * 2, st + 1, fin))
		if (st + 1) % 2 == fin % 2:
			return any(next)
		else:
			return all(next)

ans = []
for s in range(1, 150):
	if s % 3 == 0:
		continue
	else:
		if game(s, 0, 2):
			ans.append([19, s])
	if game(s, 0, 3) and not game(s, 0, 1):
		ans.append([20, s])
	if game(s, 0, 4) and not game(s, 0, 2):
		ans.append([21, s])
print(*sorted(ans), sep='\n')