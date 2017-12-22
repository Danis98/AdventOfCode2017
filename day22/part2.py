input_rows = open('day22.input').read().rstrip().split('\n')
iters = 10000000

NODE_WEAK = 0
NODE_INF = 1
NODE_FLAG = 2
NODE_CLEAN = 3

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cells = {}
pos = [len(input_rows) / 2, len(input_rows[0]) / 2]
d = 0

inf_count = 0

for i in range(0, len(input_rows)):
    row = input_rows[i]
    for j in range(0, len(row)):
        cells[(i, j)] = NODE_INF if row[j] == '#' else NODE_CLEAN

for i in range(0, iters):
    if cells[(pos[0], pos[1])] == NODE_WEAK:
        inf_count += 1
    d = (d + cells[(pos[0], pos[1])]) % 4
    cells[(pos[0], pos[1])] = (cells[(pos[0], pos[1])] + 1) % 4
    pos[0] += dy[d]
    pos[1] += dx[d]
    if (pos[0], pos[1]) not in cells:
        cells[(pos[0], pos[1])] = NODE_CLEAN

print inf_count
