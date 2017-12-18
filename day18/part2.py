instrs = open('day18.input').read().rstrip().split('\n')

regs = [{'p': 0}, {'p': 1}]
messages = [[], []]
is_locked = [False, False]
sent_count = [0, 0]

def get_val(program_id, tok):
    if (tok[0]>='0' and tok[0]<='9') or tok[0] == '-':
        return int(tok)
    else:
        if tok not in regs[program_id]:
            regs[program_id][tok] = 0
        return regs[program_id][tok]

def exec_instr(program_id, instr_ptr):
    global regs, messages, is_locked, sent_count, instrs
    ops = instrs[instr_ptr].split()
    if ops[0] == 'set':
        regs[program_id][ops[1]] = get_val(program_id, ops[2])
    elif ops[0] == 'add':
        if ops[1] not in regs[program_id]:
            regs[program_id][ops[1]] = 0
        regs[program_id][ops[1]] += get_val(program_id, ops[2])
    elif ops[0] == 'mul':
        if ops[1] not in regs[program_id]:
            regs[program_id][ops[1]] = 0
        regs[program_id][ops[1]] *= get_val(program_id, ops[2])
    elif ops[0] == 'mod':
        if ops[1] not in regs[program_id]:
            regs[program_id][ops[1]] = 0
        regs[program_id][ops[1]] %= get_val(program_id, ops[2])
    elif ops[0] == 'snd':
        messages[(program_id + 1) % 2].append(get_val(program_id, ops[1]))
        sent_count[program_id] += 1
    elif ops[0] == 'rcv':
        regs[program_id][ops[1]] = messages[program_id].pop(0)
    elif ops[0] == 'jgz':
        if get_val(program_id, ops[1]) > 0:
            instr_ptr += get_val(program_id, ops[2])
            return instr_ptr
    instr_ptr += 1
    return instr_ptr

ip0 = 0
ip1 = 0

is_locked[0] = 'rcv' in instrs[ip0] and not messages[0]
is_locked[1] = 'rcv' in instrs[ip1] and not messages[1]

while not (is_locked[0] and is_locked[1]) and not (ip0 >= len(instrs) and ip1 >= len(instrs)):
    while (not is_locked[0]) and ip0 < len(instrs):
        ip0 = exec_instr(0, ip0)
        is_locked[0] = ('rcv' in instrs[ip0] and not messages[0])
    while (not is_locked[1]) and ip1 < len(instrs):
        ip1 = exec_instr(1, ip1)
        is_locked[1] = ('rcv' in instrs[ip1] and not messages[1])
    is_locked[0] = ('rcv' in instrs[ip0] and not messages[0])
    is_locked[1] = ('rcv' in instrs[ip1] and not messages[1])

print(sent_count[1])
