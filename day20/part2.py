from Queue import PriorityQueue
from math import sqrt

particles = [[[int(val) for val in part[3:len(part)-1].split(',')] for part in line.split(', ')] for line in open('day20.input').read().rstrip().split('\n')]

max_time = 100000
elim_threshold = 100000000
to_erase = []
erased = len(particles)

for tick in xrange(0, max_time):
    for i in xrange(0, len(particles)):
        part = particles[i]
        for dim in range(0, 3):
            part[1][dim] += part[2][dim]
            part[0][dim] += part[1][dim]
    for i in range(0, len(particles)):
        if i in to_erase:
            continue
        erase_this = False
        for j in range(i+1, len(particles)):
            if particles[i][0] == particles[j][0]:
                to_erase.append(i)
                to_erase.append(j)
                erased -= 1
                erase_this = True
        if erase_this:
            to_erase.append(i)
            erased -= 1
    for i in range(0, len(particles)):
        if abs(particles[i][0][0]) > elim_threshold and abs(particles[i][0][1]) > elim_threshold and abs(particles[i][0][2]) > elim_threshold:
            to_erase.append(i)
    for ind in reversed(sorted(list(set(to_erase)))):
        particles.pop(ind)
    to_erase = []
    if tick % 1000 == 0:
        print "[%d] - %d left" % (tick, len(particles))
print len(particles)
print erased
