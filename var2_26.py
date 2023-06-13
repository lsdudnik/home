def ent(n):
	n.sort()
	m_pod = []
	for i in range(2, len(n)):
		if n[i] - n[i - 2] == 2:
			m_pod.append(n[i - 2] - 1)
		elif n[i] - n[i - 2] == 3:
			temp = min([x for x in range(n[i - 2], n[i] + 1) if x not in n])
			m_pod.append(temp)
	if len(m_pod) != 0:
		return min(m_pod)
	else:
		return False


home = dict()
for x in open('26-95.txt'):
	x = list(map(int, x.split()))
	if x[0] in home:
		home[x[0]].append(x[1])
	else:
		home[x[0]] = [x[1]]
ans = []
for item in home:
	if len(home[item]) > 2 and ent(home[item]):
		ans.append([item, ent(home[item])])
	ans.sort(reverse = True)
print(len(ans), ans[0][1])

