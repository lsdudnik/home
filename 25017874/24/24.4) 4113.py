st = open('24_4113.txt').readline().replace('B', 'D').replace('DD', '*')
st = st.replace('A', ' ').replace('D', ' ').split()
print(len(max(st, key=len)))