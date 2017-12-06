banks = [int(e) for e in open('day6.input').read().rstrip().split()]

mem = {}
time = 0
while repr(banks) not in mem:
    mem[repr(banks)] = time
    ind = banks.index(max(banks))
    banks[ind], val = 0, banks[ind]
    while val:
        banks[(ind+val)%len(banks)], val = banks[(ind+val)%len(banks)]+1, val-1
    time += 1
print time - mem[repr(banks)]
