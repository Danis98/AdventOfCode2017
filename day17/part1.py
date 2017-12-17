skip = int(open('day17.input').read().rstrip())

buf = [0]
index = 0

for i in range(1, 2017+1):
    index = (index + skip) % len(buf) + 1
    buf.insert(index, i)
print buf[(index+1) % len(buf)]
