import asyncio
import datetime

instrs = open('day18.input').read().rstrip().split('\n')

regs = [{}, {}]
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

ip = [0, 0]

async def run_program(program_id):
    global regs, messages, is_locked, sent_count, instrs
    ip[program_id] = 0
    regs[program_id]['p'] = program_id
    while ip[program_id] < len(instrs):
        ops = instrs[ip[program_id]].split()
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
            while not messages[program_id]:
                await asyncio.sleep(0.01)
                is_locked[0] = 'rcv' in instrs[ip[0]] and not messages[0]
                is_locked[1] = 'rcv' in instrs[ip[1]] and not messages[1]
                if is_locked[(program_id + 1) % 2]:
                    asyncio.get_event_loop().stop()
            regs[program_id][ops[1]] = messages[program_id].pop(0)
        elif ops[0] == 'jgz':
            if get_val(program_id, ops[1]) > 0:
                ip[program_id] += get_val(program_id, ops[2]) - 1
        ip[program_id] += 1
        await asyncio.sleep(0.000001)
        if ip[0] >= len(instrs) and ip[1] >= len(instrs):
            asyncio.get_event_loop().stop()

try:
    asyncio.get_event_loop().run_until_complete(asyncio.gather(
        run_program(0),
        run_program(1)
    ))
except:
    pass

print(sent_count[1])
