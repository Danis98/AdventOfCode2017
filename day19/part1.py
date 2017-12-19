grid = open('day19.input').read().split('\n')

for i in range(0, len(grid)):
    if len(grid[i]) > 0 and grid[i][len(grid[i]) - 1] == '\n':
        grid[i][len(grid[i]) - 1] = ' '
    while len(grid[i]) < 201:
        grid[i] += ' '

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

pos = [0, grid[0].index('|')]
d = 2

string = ""

while True:
    if grid[pos[0]][pos[1]] == '+':
        p1 = [pos[0] + dy[(d+1)%4], pos[1] + dx[(d+1)%4]]
        p2 = [pos[0] - dy[(d+1)%4], pos[1] - dx[(d+1)%4]]
        if p1[1] < 0 or p1[1] > len(grid[pos[0]]) or p1[0] < 0 or p1[0] > len(grid):
            d = (d + 3) % 4
        elif p1[1] < 0 or p1[1] > len(grid[pos[0]]) or p1[0] < 0 or p1[0] > len(grid):
            d = (d + 1) % 4
        elif d % 2 == 0:
            if grid[p1[0]][p1[1]] == '-':
                d = (d + 1) % 4
            elif grid[p2[0]][p2[1]] == '-':
                d = (d + 3) % 4
        elif d % 2 == 1:
            try:
                if grid[p1[0]][p1[1]] == '|':
                    d = (d + 1) % 4
                elif grid[p2[0]][p2[1]] == '|':
                    d = (d + 3) % 4
            except IndexError:
                print len(grid[p1[0]])
        pos[0] += dy[d]
        pos[1] += dx[d]
    elif grid[pos[0]][pos[1]] == ' ':
        break
    else:
        if grid[pos[0]][pos[1]].isalpha():
            string += grid[pos[0]][pos[1]]
        pos[0] += dy[d]
        pos[1] += dx[d]

print string
