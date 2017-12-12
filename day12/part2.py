lines = open('day12.input').read().rstrip().split('\n')

graph = [map(int, l[l.index('<-> ')+4:].split(', ')) for l in lines]
vis = [False for l in lines]

def dfs(start):
    global graph, vis
    stack = [start]
    vis[start] = True

    while len(stack)>0:
        cur = stack[len(stack)-1]
        stack.pop()
        for n in graph[cur]:
            if vis[n]:
                continue
            vis[n] = True
            stack.append(n)

cnt = 0
for i in range(0, len(graph)):
    if vis[i]:
        continue
    cnt += 1
    dfs(i)
print cnt
