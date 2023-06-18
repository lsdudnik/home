from itertools import *
from math import *
from fnmatch import fnmatch


# def f(n):
# 	if n < 3:
# 		return 1
# 	if n > 2 and n % 2 == 0:
# 		return f(n - 1) + n - 1
# 	else:
# 		return f(n - 2) + 2 * n
#
#
# print(f(24) - f(22))
# st = '8' * 128
# while '2222' in st or '888' in st:
# 	if '2222' in st:
# 		st = st.replace('2222', '8', 1)
# 	else:
# 		st = st.replace('888', '2', 1)
# print(st)
#
# ex = 3 * 1024 ** 191 + 2 * 256 ** 192 + 3 * 64 ** 193 - 2 * 16 ** 194 - 2023
# count = 0
# while ex > 0:
# 	if ex % 4 == 0:
# 		count += 1
# 	ex //= 4
# print(count)
#
# for a in range(1000):
# 	flag = 1
# 	for x in range(1000):
# 		for y in range(1000):
# 			flag *= (x < a) or (y < a) or (x + 3 * y > 180)
# 		if not flag:
# 			break
# 	if flag:
# 		print(a)
# 		break
#
# def game(h, st, fin):
# 	if h >= 91:
# 		return st % 2 == fin % 2
# 	elif st == fin:
# 		return 0
# 	else:
# 		next = [game(h + 1, st + 1, fin), game(h * 3, st + 1, fin)]
# 		if (st + 1) % 2 == fin % 2:
# 			return any(next)
# 		else:
# 			return all(next)
#
#
# for s in range(1, 91):
# 	if game(s, 0, 2):
# 		print(s)
# 		break
# for s in range(1, 91):
# 	if game(s, 0, 3) and not game(s, 0, 1):
# 		print(s)
# for s in range(1, 91):
# 	if game(s, 0, 4) and not game(s, 0, 2):
# 		print(s)

# num = [int(x) for x in open('1_17 (1).txt')]
# mx = max([x for x in num if str(x)[-1] == '5'])
# ans = []
# for i in range(1, len(num)):
# 	if str(num[i])[-1] == '5' or str(num[i - 1])[-1] == '5':
# 		if (num[i] - num[i - 1]) ** 2 < mx ** 2:
# 			ans.append((num[i] - num[i - 1]) ** 2)
# print(len(ans), min(ans))


# def f(x, y, z, w):
# 	return (y <= z) and (w != z) and x
#
# for var in product([0, 1], repeat = 4):
# 	tab = [(0, var[0], 0, 1), (var[1], 0,  var[2], var[3]), (1, 0, 0, 1)]
# 	if len(tab) == len(set(tab)):
# 		for p in permutations('xywz'):
# 			if [f(**dict(zip(p, row))) for row in tab] == [1, 1, 1]:
# 				print(*p, sep = '')

# ind = 39 * ceil(log(900 + 10, 2))
# ind = ceil(ind / 8)
# print((ind * 65536) / 2014)

# comb = list(map(''.join, product('ажзилю', repeat = 6)))
# for i in range(len(comb)):
# 	if comb[i][0] != 'ю' and comb[i].count('ж') == 1 and comb[i].count('л') <= 1:
# 		print(i + 1, comb[i])

# print(240 * 2 * (1/3) * (1/2))

# count = 0
# for item in open('9'):
# 	item = sorted(list(map(int, item.split())))
# 	if len(item) == len(set(item)):
# 		if item[0] + item[-1] == sum(item[1:-1]):
# 			count += 1
# print(count)

# def f(st, fin):
# 	if st == fin:
# 		return 1
# 	if st > fin or st == 24:
# 		return 0
# 	else:
# 		return f(st + 1, fin) + f(st * 3, fin)
# print(f(2, 6) * f(6, 61))

# for x in range(129, 10 ** 8, 129):
# 	if fnmatch(str(x), '123?4*6'):
# 		print(x, x //129)
# ans = []
# for n in range(1, 1000):
# 	n2 = bin(n)[2:]
# 	if n2.count('1') % 2 == 0:
# 		n2 = '11' + n2[2:] + '0'
# 	else:
# 		n2 = '11' + n2[2:] + '1'
# 	if int(n2, 2) <= 57:
# 		ans.append([int(n2, 2), n])
# print(sorted(ans, reverse = True))
