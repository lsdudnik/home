for n in range(1, 10000):
	n2 = bin(n)[2:]
	n2 = n2.replace('1', '*')
	n2 = n2.replace('0', '1')
	n2 = n2.replace('*', '0')
	if (n - int(n2, 2)) == 979:
		print(n)
		break