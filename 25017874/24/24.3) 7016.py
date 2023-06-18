st = open('24_7016.txt').readline().split('A')
mx = 0
for item in st:
	right, left = item.find('D'), item.rfind('D')
	if right != -1:
		mx = max(mx, len(item[:right + 1]))
	if left != -1:
		mx = max(mx, len(item[left:]))
print(mx + 1)


