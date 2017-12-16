import string

moves = open('day16.input').read().rstrip().split(',')

num_progs = 16
reps = 1000000000
state = [chr(ord('a') + i) for i in range(0, num_progs)]
state_inv = {chr(ord('a') + i): i for i in range(0, num_progs)}
offset = 0

sparse_table = []

mem = []

while state not in mem:
    mem.append([ch for ch in state])
    for move in moves:
        if move[0] == 's':
            offset = (offset - int(move[1:], 10) + num_progs) % num_progs
        elif move[0] == 'x':
            p1 = (int(move[1:move.index('/')], 10)+offset) % num_progs
            p2 = (int(move[move.index('/')+1:], 10)+offset) % num_progs
            temp = state[p1]
            state[p1] = state[p2]
            state[p2] = temp
            state_inv[state[p1]] = p1
            state_inv[state[p2]] = p2
        elif move[0] == 'p':
            p1 = (state_inv[move[1]]) % num_progs
            p2 = (state_inv[move[3]]) % num_progs
            temp = state[p1]
            state[p1] = state[p2]
            state[p2] = temp
            state_inv[state[p1]] = p1
            state_inv[state[p2]] = p2

reps -= mem.index(state)
reps %= (len(mem)-mem.index(state))
print ''.join(mem[reps])
