file = open('7891').readline()
let = [chr(i) for i in range(ord('A'), ord('Z')+1)]
mx = 0
for item in let:
	st = file.split(item)
	cur_max = len(max(st, key=len))
	mx = max(mx, cur_max)
print(mx + 2)