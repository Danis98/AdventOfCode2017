jmps = [int(e) for e in open('day5.input').read().rstrip().split()]

pos = 0
time = 0
while pos >= 0 and pos < len(jmps):
    jmps[pos] += 1
    pos += jmps[pos] - 1
    time +=1
print time
