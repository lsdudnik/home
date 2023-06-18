from fnmatch import *

for n in range(2023, 10 ** 8, 2023):
	if fnmatch(str(n), '11????11') and int(str(n)[2]) % 2 == 0 and int(str(n)[-3]) % 2 != 0:
		print(n, n // 2023)
