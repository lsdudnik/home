# k = 2
# data = open('26_test.txt')
k = 150
data = open('26_8482.txt')
table = [[i, 0] for i in range(k)]
close = 23 * 60
cl = dict()
last, count = 0, 0
for line in data:
	cur = list(map(int, line.split()))
	if cur[0] not in cl:
		cl[cur[0]] = [cur[1]]
	else:
		cl[cur[0]].append(cur[1])

arv = sorted(cl)

def free(p, table):
	for i in range(len(table)):
		if table[i][1] == 0:
			return table[i][0]
	return 'full'
def min_wait(p, tab):
	need_tab = 0
	wait = 10000000
	for i in range(len(tab)):
		if tab[i][1] <= p + 10 and tab[i][1] != 0:
			if tab[i][1] - p  < wait:
				wait = tab[i][1] - p
				need_tab = tab[i][0]
	if wait > 10000000:
		return 'full'
	else:
		return [need_tab, wait]
test2 = []
for time_ar in arv:
	if time_ar == 445:
		print()
	out = sorted(cl[time_ar])

	while len(out) > 0:
		if free(time_ar, table) != 'full' and out[0] <= close and min_wait(time_ar, table)[1] != 0:
			last = free(time_ar, table) + 1
			table[free(time_ar, table)][1] = out[0] + 5 + 1
			count += 1
			test2.append([count, last, time_ar, out[0]])
			out.pop(0)
		elif min_wait(time_ar, table) != 'full' and out[0] + min_wait(time_ar, table)[1] <= close :
			last = min_wait(time_ar, table)[0] + 1
			temp = min_wait(time_ar, table)[1]
			table[min_wait(time_ar, table)[0]][1] = out[0] + 5 + 1 + min_wait(time_ar, table)[1]
			count += 1
			test2.append([count, last, time_ar, out[0]])
			out.pop(0)
		else:
			out.pop(0)
print(count, last)
