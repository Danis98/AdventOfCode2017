particles = [[[int(val) for val in part[3:len(part)-1].split(',')] for part in line.split(', ')] for line in open('day20.input').read().rstrip().split('\n')]

max_acc = 999999
max_ind = -1
for ind in xrange(0, len(particles)):
    part = particles[ind]
    acc = abs(part[2][0]) + abs(part[2][1]) + abs(part[2][2])
    if acc < max_acc:
        max_ind = ind
        max_acc = acc
    if acc == max_acc:
        print (ind, part)

print max_ind
