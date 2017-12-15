state = [int(l.split()[4]) for l in open('day15.input').read().rstrip().split('\n')]

coeff = [16807, 48271]
mod = 2147483647

count = 0
for i in range(0, 40000000):
    state[0] = (state[0] * coeff[0]) % mod
    state[1] = (state[1] * coeff[1]) % mod
    if state[0] & 0xffff == state[1] & 0xffff:
        count += 1
print count
