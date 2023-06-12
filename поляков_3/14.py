ss55 = [str(i) for i in range(10)] + [chr(x) for x in range(ord('A'), ord('Z') + 1)]


def s(n):
	su = 0
	n = n[::-1]
	for i in range(len(n)):
		su += ss55.index(n[i]) * 55 ** i
	return su
ans = []
for a in range(55):
	s1 = s('Z0YX') + a * 55 ** 2
	s2 = s('2X0Y') + a * 55
	if (s1 - s2) % 29 == 0:
		ans.append(s1 - s2)

print(abs(min(ans) - max(ans)))
