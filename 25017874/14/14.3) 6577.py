ex = 673 ** 7 + 67 ** 6 + 3 ** 3
dig = []
while ex > 0:
	dig.append(hex(ex % 12)[2:])
	ex //= 12
print(dig.count('a') * 10 - dig.count('8') * 8)