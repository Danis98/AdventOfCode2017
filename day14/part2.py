key = open('day14.input').read().rstrip()

grid_size = 128

grid = [['.' for i in range(0, grid_size)] for j in range(0, grid_size)]
vis = [[False for i in range(0, grid_size)] for j in range(0, grid_size)]

def knot_hash(in_str):
    in_seq = [ord(ch) for ch in in_str]
    in_seq += [17, 31, 73, 47, 23]

    list_len = 256
    nums = range(0, list_len)

    index = 0
    skip = 0

    for round_num in range(0, 64):
        for l in in_seq:
            arr = (nums[index:index+l] if index+l<list_len else nums[index:list_len]+nums[:(index+l)%list_len])[::-1]
            for i in range(index, index+l):
                nums[i%list_len] = arr[i-index]
            index = (index+l+skip)%list_len
            skip += 1

    final_hash = ''.join(["%02x"%n for n in [reduce(lambda i, j: int(i) ^ int(j), nums[i*16:(i+1)*16]) for i in range(0, 16)]])

    return final_hash

def dfs(start, ind):
    global grid, vis
    stack = [start]
    vis[start[0]][start[1]] = True

    while len(stack)>0:
        cur = stack[len(stack)-1]
        stack.pop()
        r = cur[0]
        c = cur[1]
        grid[r][c] = ind
        if c>0 and grid[r][c-1] != '.' and not vis[r][c-1]:
            vis[r][c-1] = True
            stack.append((r, c-1))
        if r>0 and grid[r-1][c] != '.' and not vis[r-1][c]:
            vis[r-1][c] = True
            stack.append((r-1, c))
        if c<grid_size-1 and grid[r][c+1] != '.' and not vis[r][c+1]:
            vis[r][c+1] = True
            stack.append((r, c+1))
        if r<grid_size-1 and grid[r+1][c] != '.' and not vis[r+1][c]:
            vis[r+1][c] = True
            stack.append((r+1, c))

for i in range(0, grid_size):
    row_hash=int(knot_hash("%s-%d" % (key, i)), 16)
    j = 0
    while row_hash>0:
        if row_hash % 2 == 1:
            grid[i][grid_size-1-j] = '#'
        j += 1
        row_hash /= 2

regions = 0
for i in range(0, grid_size):
    for j in range(0, grid_size):
        if grid[i][j] == '.' or vis[i][j]:
            continue
        regions += 1
        dfs((i, j), str(regions))
print regions
