ans = set()
def f(cur, step):
	if step == 7:
		ans.add(cur)
	else:
		f(cur + 1, step + 1)
		f(cur + 2, step + 1)
		f(cur * 2, step + 1)

f(1, 0)
# print(ans)

print(len(ans))
