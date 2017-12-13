firewall = {}
for l in open('day13.input').read().rstrip().split('\n'):
    firewall[int(l.split(': ')[0])] = int(l.split(': ')[1])

severity = 0

for lev in firewall:
    if lev % (2*firewall[lev] -2 ) == 0:
        severity += lev * firewall[lev]

print severity
