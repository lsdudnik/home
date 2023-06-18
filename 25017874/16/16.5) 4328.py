f = [0, 1, 1]
for n in range(3, 58):
	f.append(f[n - 1] + f[n - 2] + 1)
print(f[57])
