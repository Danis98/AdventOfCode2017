seq = open('day1.input').read().rstrip()

sum = 0
for i in range(0, len(seq)):
    if seq[i] == seq[(i+1)%len(seq)]:
        sum += int(seq[i])
print sum
