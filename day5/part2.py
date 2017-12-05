jmps = [int(e) for e in open('day5.input').read().rstrip().split()]

pos = 0
time = 0
while pos >= 0 and pos < len(jmps):
    oldjmp = jmps[pos]
    jmps[pos] += 1 if jmps[pos] < 3 else -1
    pos += oldjmp
    time +=1
print time
