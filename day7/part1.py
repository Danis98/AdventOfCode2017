input_lines = open('day7.input').read().rstrip().split('\n')

weight = {}
par ={}

for line in input_lines:
    p = line[:line.index(' ')]
    w = int(line[line.index("(") + 1:line.rindex(")")])
    weight[p] = w
    if '->' in line:
        for ch in line[line.index('>')+2:].rstrip().split(', '):
            par[ch] = p

cur = input_lines[0][:line.index(' ')]
while cur in par:
    cur = par[cur]
print cur
