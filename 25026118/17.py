num = [int(x) for x in open('17_8475.txt')]
m = min([y for y in num if (str(y)[-1] == '8' and len(str(abs(y))) == 3)]) ** 2
# print(m)
ans = []

def tr(x):
	for y in x:
		if len(str(abs(y))) == 3:
			return True

for i in range(2, len(num)):
	temp = num[i - 2:i + 1]
	count = 0
	for item in temp:
		if item ** 2 > m:
			count += 1
	if count == 2 and tr(temp):
		ans.append(sum(temp))
print(len(ans), max(ans))
