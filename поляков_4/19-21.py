def game(h1, h2, st, fin):
	# условие победы
	if h1 + h2 >= 259:
		return st % 2 == fin % 2
	# конец без победы
	elif st == fin:
		return 0
	else:
		next = [game(h1 + 1, h2, st + 1, fin), game(h1 * 2, h2, st + 1, fin), \
		        game(h1, h2 + 1, st + 1, fin), game(h1, h2 * 2, st + 1, fin)]
		if (st + 1) % 2 == fin % 2:
			return any(next)
		else:
			return all(next)

for s in range(1, 242):
	if game(17, s, 0, 4) and not game(17, s, 0, 2):
		print(s)
