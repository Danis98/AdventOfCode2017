skip = int(open('day17.input').read().rstrip())

num_iters = 50000000

buf = [-1 for i in range(0, num_iters+1)]
buf[0] = 0
index = 0
length = 1

for i in range(1, num_iters+1):
    index = (index + skip) % length + 1
    buf[index] = i
    length += 1
print buf[(buf.index(0) + 1)%length]
