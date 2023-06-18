ans = set()
def f(cur, step):
	if step == 7:
		ans.add(cur)
	if step > 7:
		return 0
	f(cur + 1, step + 1)
	f(cur + 2, step + 1)
	f(cur * 2, step + 1)

f(1, 0)
# print(ans)
for i in range(2, 1000):
	if i not in ans:
		print(i)
		break