instrs = open('day8.input').read().rstrip().split('\n')

regs = {}
m = 0

for instr in instrs:
    words = instr.split()
    reg_id = words[0]
    op = words[1]
    val = int(words[2])
    cmp_reg = words[4]
    cmp = words[5]
    cmp_val = int(words[6])

    if reg_id not in regs:
        regs[reg_id] = 0
    if cmp_reg not in regs:
        regs[cmp_reg] = 0

    if cmp == '==':
        if regs[cmp_reg] != cmp_val:
            continue
    elif cmp == '!=':
        if regs[cmp_reg] == cmp_val:
            continue
    elif cmp == '>=':
        if regs[cmp_reg] < cmp_val:
            continue
    elif cmp == '<=':
        if regs[cmp_reg] > cmp_val:
            continue
    elif cmp == '>':
        if regs[cmp_reg] <= cmp_val:
            continue
    elif cmp == '<':
        if regs[cmp_reg] >= cmp_val:
            continue

    if op == 'inc':
        regs[reg_id] += val
    if op == 'dec':
        regs[reg_id] -= val

    m = max([m, max(regs.values())])

print m
