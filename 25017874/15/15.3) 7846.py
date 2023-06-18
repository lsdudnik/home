p = [x for x in range(13, 20)]
q = [x for x in range(17, 24)]
ans = []
for a in range(0, 100):
    f = 1
    for x in range(100):
        f *= (not(not(x in p) <= (x in q))) <= ((x == a) <= ((not(x in q)) <= (x in p)))
        if not f:
            break
    if f:
        ans.append(a)

for i in range(100):
    if i in ans:
        print(i, end=' ')
    else:
        print(' ', end=' ')
