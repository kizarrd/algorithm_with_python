from collections import deque

n, m, start = map(int, input().split())
vertexList = [ [] for _ in range(n+1) ]
check = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    vertexList[u].append(v)
    vertexList[v].append(u)
for i in range(1, n+1):
    vertexList[i].sort()  

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for adjacentVertex in vertexList[x]:
        if check[adjacentVertex] == False:
            dfs(adjacentVertex)

def bfs(x):
    check = [False]*(n+1)
    q = deque()
    q.append(x)
    check[x] = True
    while q:
        next_vertex = q.popleft()
        print(next_vertex, end=' ')
        for adjacentVertex in vertexList[next_vertex]:
            if check[adjacentVertex] == False:
                check[adjacentVertex] = True
                q.append(adjacentVertex)

dfs(start)
print()
bfs(start)