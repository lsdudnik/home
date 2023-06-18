def game(h1, h2, st, fin):
	if h1 + h2 >= 255:
		return st % 2 == fin % 2
	elif st == fin:
		return 0
	else:
		next = [game(h1 + 1, h2, st + 1, fin), game(h1 * 2, h2, st + 1, fin), game(h1, h2 + 1, st + 1, fin), game(h1, h2 * 2, st + 1, fin)]
		if (st + 1) % 2 == fin % 2:
			return any(next)
		else:
			return all(next)

ans = []
for s in range(1, 238):
	if game(17, s, 0, 2):
		print(f'19: {s}')
		break

for s in range(1, 238):
	if game(17, s, 0, 3) and not game(17, s, 0, 1):
		ans.append([20, s])
	if game(17, s, 0, 4) and not game(17, s, 0, 2):
		ans.append([21, s])
print(*sorted(ans), sep='\n')