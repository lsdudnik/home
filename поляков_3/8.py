from itertools import product

#  антиутопия = ы
comb = list(map(''.join, product('антиуопяы', repeat = 7)))
count = 0
for item in comb:
	if item[0] != 'а' and item[-1] != 'я':
		if 'ы' in item and item[0] != 'ы' and item[-1] != 'ы' and item.count('ы') == 1:
			count += 1
print(count)
