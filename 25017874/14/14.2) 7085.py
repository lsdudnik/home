ex = 3 * 625 ** 173 + 4 * 125 ** 180 + 3 * 25 ** 157 + 2 * 5 ** 155 + 156
count = 0
while ex > 0:
	if ex % 25 == 0:
		count += 1
	ex //= 25
print(count)
