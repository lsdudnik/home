st = open('24_3021.txt').readline().replace('ZXY', '*').replace('ZYX', '*')
st = st.replace('Z', ' ').replace('Y', ' ').replace('X', ' ').split()
print(len(max(st, key=len)))