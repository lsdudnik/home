num = [int(x) for x in open('6696')]

ans = []
for i in range(2, len(num)):
	temp = num[i - 2: i + 1]
	if num[i] > 0 or num[i - 1] > 0 or num[i - 2] > 0:
		if sum(temp) % 2022 == 0:
			ans.append(sum(temp))

print(len(ans), max(ans))
