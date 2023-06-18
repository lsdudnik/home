def game(h, st, fin):
	if h <= 10:
		return st % 2 == fin % 2
	elif st == fin:
		return 0
	else:
		next = [game(h // 3, st + 1, fin), game(h - 10, st + 1, fin)]
		if (st + 1) % 2 == fin % 2:
			return any(next)
		else:
			return all(next)

ans20, count21 = [], 0
for s in range(300, 0, -1):
	if game(s, 0, 2):
		print(f'19: {s}')
		break
for s in range(300, 0, -1):
	if game(s, 0, 3) and not game(s, 0, 1):
		ans20.append([20, s])
	if game(s, 0, 4) and not game(s, 0, 2):
		count21 += 1
print(*sorted(ans20), sep='\n')
print(count21)