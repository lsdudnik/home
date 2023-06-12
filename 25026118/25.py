from fnmatch import *

for n in range(237, 10 ** 8, 237):
	if fnmatch(str(n), '81?2*80') and not fnmatch(str(n), '*9*'):
		print(n, n // 237)
