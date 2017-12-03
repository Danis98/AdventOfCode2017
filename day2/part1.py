rows = [[int(e) for e in r.split()] for r in open('day2.input').read().rstrip().split('\n')]

checksum = 0
for r in rows:
    checksum += max(r) - min(r)
print checksum
