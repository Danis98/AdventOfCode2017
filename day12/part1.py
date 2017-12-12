lines = open('day12.input').read().rstrip().split('\n')

graph = [map(int, l[l.index('<-> ')+4:].split(', ')) for l in lines]
vis = [False for l in lines]

start = 0
cnt = 0
stack = [start]
vis[start] = True

while len(stack)>0:
    cur = stack[len(stack)-1]
    stack.pop()
    cnt += 1
    for n in graph[cur]:
        if vis[n]:
            continue
        vis[n] = True
        stack.append(n)
print cnt
