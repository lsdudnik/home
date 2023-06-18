from math import *

# 8499
ind = ceil(213 * 11 / 8)
print(ind * 16384 / 2 ** 10)

# 3169
ind1 = 15 * 5
ind2 = ceil(log(9999, 2))
full = ceil((ind1 + ind2) / 8)
print(int(1600 / (full + 12)))

# 1053
frame1 = ceil(log(10_000, 2))
frame2 = 80 * ceil(log((33 + 33 + 2), 2))
frame3 = 20 * ceil(log((26 + 9), 2))
print((ceil(frame1 / 8) + ceil(frame2 / 8) + ceil(frame3 / 8)) * 25)

# 671
pas = ceil(10 * 5 / 8)
full = pas + 15
print(int((4 * 2 ** 10) / full))

# 428
pas = ceil(log((26 * 2 + 10 + 4) ** 11, 2))
pas = ceil(pas / 8)
mail = 22 * 5
mail = ceil(mail / 8)
one = 600 / 20
print(one - pas - mail)

# 137
code = 14 * ceil(log(36, 2))
code = ceil(code / 8)
# abcdef 9
part = log(33333444, 2)
part = ceil(part / 8)
print(30 - code - part)

# 463
no_sim = 4 + 4 + 4 * 3 + 4
no_def = 7 + 10 + 4
print(no_def - no_sim)


