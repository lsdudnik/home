In = 1600 * 1920 * 8
Ie = 4 * 32_000 * 8 * 104
dif = abs(In - Ie)
q = 100 * 2 ** 13
print(min(Ie, In) / (q / 2) + (dif / q))