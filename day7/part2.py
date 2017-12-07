input_lines = open('day7.input').read().rstrip().split('\n')

weight = {}
childs = {}
par = {}

for line in input_lines:
    p = line[:line.index(' ')]
    w = int(line[line.index("(") + 1:line.rindex(")")])
    weight[p] = w
    if '->' in line:
        if p not in childs:
            childs[p] = []
        for ch in line[line.index('>')+2:].rstrip().split(', '):
            par[ch] = p
            childs[p].append(ch)

root = input_lines[0][:line.index(' ')]
while root in par:
    root = par[root]

def check_balance(node):
    balances = {}
    if node not in childs:
        return weight[node]
    for ch in childs[node]:
        tow_w = check_balance(ch)
        if tow_w is None:
            return None
        balances[ch] = tow_w
    if len(set(balances.values())) == 1:
        return weight[node] + sum(balances.values())
    else:
        exp = max(set(balances.values()), key=balances.values().count)
        for ch in balances:
            if balances[ch] != exp:
                print weight[ch]+(exp-balances[ch])
                return None

check_balance(root)
