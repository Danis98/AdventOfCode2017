cmds = open('day11.input').read().rstrip().split(',')

off = {
    'n': (0, 1),
    's': (0, -1),
    'se': (1, -.5),
    'ne': (1, .5),
    'sw': (-1, -.5),
    'nw': (-1, .5)
}

pos = (0, 0)
maxd = 0
for cmd in cmds:
    pos = tuple(map(sum, zip(pos, off[cmd])))
    dx, dy = float(abs(pos[0])), float(abs(pos[1]))
    dist = dx + ((dy-dx/2) if dy>dx else 0)
    maxd = max(maxd, dist)

print maxd
