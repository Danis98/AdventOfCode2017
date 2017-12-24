import time

instrs = open('day23.input').read().rstrip().split('\n')

regs = {
    'a': 1
}
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
    elif ops[0] == 'sub':
        if ops[1] not in regs:
            regs[ops[1]] = 0
        regs[ops[1]] -= get_val(ops[2])
    elif ops[0] == 'mul':
        if ops[1] not in regs:
            regs[ops[1]] = 0
        regs[ops[1]] *= get_val(ops[2])
    elif ops[0] == 'jnz':
        if get_val(ops[1]) != 0:
            instr_ptr += get_val(ops[2]) - 1
    instr_ptr += 1

print regs
