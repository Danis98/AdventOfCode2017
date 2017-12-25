blueprint = [line.rstrip('\n.:').split() for line in open('day25.input').read().rstrip().split('\n')]
iters = int(blueprint[1][5])

state = blueprint[0][3]
cursor = 0

tape = {}
states = {}

for i in range(3, len(blueprint), 10):
    s = blueprint[i][2]
    states[(s, 0)] = (int(blueprint[i+2][4]), -1 if blueprint[i+3][6] == 'left' else 1, blueprint[i+4][4])
    states[(s, 1)] = (int(blueprint[i+6][4]), -1 if blueprint[i+7][6] == 'left' else 1, blueprint[i+8][4])

for i in xrange(0, iters):
    if cursor not in tape:
        tape[cursor] = 0
    new_state = states[(state, tape[cursor])]
    tape[cursor] = new_state[0]
    cursor += new_state[1]
    state = new_state[2]
print sum(tape.values())
