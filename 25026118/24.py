file = open('24_8480.txt').readline()
forb = 'ABC'
for item in forb:
	file = file.replace(item, '*')
fr = [x for x in file.split('**') if len(x) > 0]
mx = max(fr, key=len)

print(len(mx) + 2)