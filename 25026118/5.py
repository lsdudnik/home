r = 1_000_000
for n in range(1, 1000000):
	n2 = bin(n)[2:]
	if n % 5 == 0:
		n2 = n2[:3] + n2
	else:
		# ost = n % 3 * 5
		# ost = bin(ost)[2:]
		# n += ost
		n2 += bin(n % 3 * 5)[2:]   
	if int(n2, 2) < r and int(n2, 2) > 39_000:
		r = int(n2, 2)
print(r)
