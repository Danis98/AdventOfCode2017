instrs = open('day18.input').read().rstrip().split('\n')

regs = {}
instr_ptr = 0

def get_val(tok):
    if (tok[0]>='0' and tok[0]<='9') or tok[0] == '-':
        return int(tok)
    else:
        if tok not in regs:
            regs[tok] = 0
        return regs[tok]

while instr_ptr < len(instrs):
    ops = instrs[instr_ptr].split()
    if ops[0] == 'set':
        regs[ops[1]] = get_val(ops[2])
    elif ops[0] == 'add':
        if ops[1] not in regs:
            regs[ops[1]] = 0
        regs[ops[1]] += get_val(ops[2])
    elif ops[0] == 'mul':
        if ops[1] not in regs:
            regs[ops[1]] = 0
        regs[ops[1]] *= get_val(ops[2])
    elif ops[0] == 'mod':
        if ops[1] not in regs:
            regs[ops[1]] = 0
        regs[ops[1]] %= get_val(ops[2])
    elif ops[0] == 'snd':
        last_played_sound = get_val(ops[1])
    elif ops[0] == 'rcv':
        if get_val(ops[1]) != 0:
            print last_played_sound
            break
    elif ops[0] == 'jgz':
        if get_val(ops[1]) > 0:
            instr_ptr += get_val(ops[2]) - 1
    instr_ptr += 1
