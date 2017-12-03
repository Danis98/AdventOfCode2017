rows = [[int(e) for e in r.split()] for r in open('day2.input').read().rstrip().split('\n')]

checksum = 0
for r in rows:
    r=sorted(r)
    f =False
    for i in range(0, len(r)):
        if f:
            break
        for j in range(i+1, len(r)):
            if f:
                break
            if r[j]%r[i] == 0:
                checksum += r[j] / r[i]
                f = True
print checksum
