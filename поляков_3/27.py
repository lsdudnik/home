from math import ceil
# 409 69383
data = open('27_3_test.txt')
# data = open('27_3(a).txt')
# data = open('27_3(b).txt')
conditions = list(map(int, data.readline().split()))
n_home, km, v, dist = conditions[0], conditions[1], conditions[2], conditions[3]
road = [0] * (km + 1)
for item in data:
	temp = list(map(int, item.split()))
	road[temp[0]] = ceil(temp[1] / v)
road += road[1:int(len(road) / 2)]
cur_sum = sum(road[:(dist * 2) + 1])
all_ans = [[cur_sum, dist]]
for i in range(dist + 1, len(road) - dist - 1):
	left = i - dist - 1
	right = i + dist
	cur_sum += road[right] - road[left]
	if road[i] != 0:
		if i < km:
			all_ans.append([cur_sum, i])
		else:
			all_ans.append([cur_sum, i - km])
print((all_ans))
