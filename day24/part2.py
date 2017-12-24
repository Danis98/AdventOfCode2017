pieces = [(int(piece.split('/')[0]), int(piece.split('/')[1])) for piece in open('day24.input').read().rstrip().split('\n')]

used = [False for piece in pieces]

max_strength = 0

def build_bridge(cur_end):
    global used
    strength = 0
    length = 0
    for i in range(0, len(pieces)):
        if used[i]:
            continue
        piece = pieces[i]
        if piece[0] == cur_end:
            used[i] = True
            n_length , n_strength = build_bridge(piece[1])
            if length < n_length + 1:
                length = n_length + 1
                strength = n_strength + cur_end + piece[1]
            elif length == n_length + 1 and strength < n_strength + piece[1] + cur_end:
                strength = n_strength + cur_end + piece[1]
            used[i] = False
        elif piece[1] == cur_end:
            used[i] = True
            n_length , n_strength = build_bridge(piece[0])
            if length < n_length + 1:
                length = n_length + 1
                strength = n_strength + cur_end + piece[0]
            elif length == n_length + 1 and strength < n_strength + piece[0] + cur_end:
                strength = n_strength + cur_end + piece[0]
            used[i] = False
    return length, strength

print build_bridge(0)[1]
