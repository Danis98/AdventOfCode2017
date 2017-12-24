pieces = [(int(piece.split('/')[0]), int(piece.split('/')[1])) for piece in open('day24.input').read().rstrip().split('\n')]

used = [False for piece in pieces]

max_strength = 0

def build_bridge(cur_end):
    strength = 0
    for i in range(0, len(pieces)):
        if used[i]:
            continue
        piece = pieces[i]
        if piece[0] == cur_end:
            used[i] = True
            strength = max([strength, build_bridge(piece[1]) + piece[1] + cur_end])
            used[i] = False
        elif piece[1] == cur_end:
            used[i] = True
            strength = max([strength, build_bridge(piece[0]) + piece[0] + cur_end])
            used[i] = False
    return strength

print build_bridge(0)
