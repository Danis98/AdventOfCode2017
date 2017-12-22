input_rows = open('day22.input').read().rstrip().split('\n')
iters = 10000

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cells = {}
pos = [len(input_rows) / 2, len(input_rows[0]) / 2]
d = 0

inf_count = 0

for i in range(0, len(input_rows)):
    row = input_rows[i]
    for j in range(0, len(row)):
        cells[(i, j)] = (row[j] == '#')

for i in range(0, iters):
    if not cells[(pos[0], pos[1])]:
        inf_count += 1
    if cells[(pos[0], pos[1])]:
        d = (d + 1) % 4
    else:
        d = (d + 3) % 4
    cells[(pos[0], pos[1])] = not cells[(pos[0], pos[1])]
    pos[0] += dy[d]
    pos[1] += dx[d]
    if (pos[0], pos[1]) not in cells:
        cells[(pos[0], pos[1])] = False

print inf_count
