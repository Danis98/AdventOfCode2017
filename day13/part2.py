firewall = {}
for l in open('day13.input').read().rstrip().split('\n'):
    firewall[int(l.split(': ')[0])] = int(l.split(': ')[1])

def check_firewall(delay):
    global firewall
    for lev in firewall:
        if (lev+delay) % (2*firewall[lev] -2 ) == 0:
            return False
    return True

delay = 0
while not check_firewall(delay):
    delay += 1
print delay
