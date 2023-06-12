from math import *
def f(dig, st, fin, limit):
    if (floor(dig * 1.25) > limit) and (floor(dig * 1.5) > limit) and (floor(dig * 1.75) > limit) and (floor(dig * 2.1) > limit):
        return (st - 1) % 2 == fin % 2
    if st == fin:
        return 0
    # val = [1.25, 1.5, 1.75, 2.1]
    # next = []
    # for item in val:
    #     if floor(dig * item) <= limit:
    #         next.append(f(floor(dig * item), st + 1, fin, limit))
    next = [f(floor(dig * 1.25), st + 1, fin, limit), f(floor(dig * 1.5), st + 1, fin, limit),
         f(floor(dig * 1.75), st + 1, fin, limit), f(floor(dig * 2.1), st + 1, fin, limit)]
    if st % 2 == fin % 2:
        return any(next)
    else:
        return all(next)


for s in range(4, 173):
    if f(s, -1, 2, s + 215):
        print(s)
# везде делаем шаг -1 и вводим предел