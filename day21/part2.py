matrix = [['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']]
iters = 18

def get_matrix(mat_str):
    mat = []
    for l in mat_str.split('/'):
        mat.append([ch for ch in l])
    return mat

rules = [(get_matrix(line[:line.index(' ')]), get_matrix(line[line.index(' => ')+4:])) for line in open('day21.input').read().rstrip().split('\n')]

def rot_2(mat):
    return [
        [mat[1][0], mat[0][0]],
        [mat[1][1], mat[0][1]]
    ]

def rot_3(mat):
    return [
        [mat[2][0], mat[1][0], mat[0][0]],
        [mat[2][1], mat[1][1], mat[0][1]],
        [mat[2][2], mat[1][2], mat[0][2]]
    ]

def flip_2(mat):
    return [
        [mat[0][1], mat[0][0]],
        [mat[1][1], mat[1][0]]
    ]

def flip_3(mat):
    return [
        [mat[0][2], mat[0][1], mat[0][0]],
        [mat[1][2], mat[1][1], mat[1][0]],
        [mat[2][2], mat[2][1], mat[2][0]]
    ]

def check_match(mat, rule):
    for i in range(0, 4):
        if mat == rule:
            return True
        if len(mat) == 2:
            mat = rot_2(mat)
        elif len(mat) == 3:
            mat = rot_3(mat)
    if len(mat) == 2:
        mat = flip_2(mat)
    elif len(mat) == 3:
        mat = flip_3(mat)
    for i in range(0, 4):
        if mat == rule:
            return True
        if len(mat) == 2:
            mat = rot_2(mat)
        elif len(mat) == 3:
            mat = rot_3(mat)
    if len(mat) == 2:
        mat = flip_2(mat)
    elif len(mat) == 3:
        mat = flip_3(mat)
    return False

def slice_mat(i, j, l):
    return [[matrix[a][b] for b in range(j, j+l)] for a in range(i, i+l)]

def apply_iter():
    global matrix
    cur_len = len(matrix)
    new_len = cur_len / 2 * 3 if cur_len % 2 == 0 else cur_len / 3 * 4
    n_mat = [[' ' for i in range(0, new_len)] for j in range(0, new_len)]
    if cur_len % 2 == 0:
        for i in range(0, cur_len/2):
            for j in range(0, cur_len/2):
                m = slice_mat(i*2, j*2, 2)
                for rule in rules:
                    if check_match(m, rule[0]):
                        m = rule[1]
                        for r in range(0, 3):
                            for c in range(0, 3):
                                n_mat[i*3+r][j*3+c] = m[r][c]
                        break
    elif cur_len % 3 == 0:
        for i in range(0, cur_len/3):
            for j in range(0, cur_len/3):
                m = slice_mat(i*3, j*3, 3)
                for rule in rules:
                    if check_match(m, rule[0]):
                        m = rule[1]
                        for r in range(0, 4):
                            for c in range(0, 4):
                                n_mat[i*4+r][j*4+c] = m[r][c]
                        break
    matrix = list(n_mat)

for i in range(0, iters):
    apply_iter()

on_cnt = 0
for row in matrix:
    for ch in row:
        if ch == '#':
            on_cnt += 1

print on_cnt
