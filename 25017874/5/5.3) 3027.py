count = 0
for n in range(1, 1000):
	n2 = bin(n)[2:]
	if n % 2 == 0:
		n2 += bin(n2.count('1'))[2:]
	else:
		n2 = '1' + n2 + '00'
	if 500 <= int(n2, 2) <= 700:
		count += 1
print(count)
