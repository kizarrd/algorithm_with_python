from collections import deque
n,m,start = map(int,input().split())
edges = []
check = [False] * (n+1)
for _ in range(m):
    u,v = map(int,input().split())
    edges.append((u,v))
    edges.append((v,u))
m *= 2
edges.sort()
cnt = [0]*(n+1)

for u, v in edges:
    cnt[u] += 1

for i in range(1, n+1):
    cnt[i] += cnt[i-1]

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for i in range(cnt[x-1],cnt[x]):
        y = edges[i][1]
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(cnt[x-1],cnt[x]):
            y = edges[i][1] 
            # edge is the list of tuple, therefore edges[i][1] indicates the starting vertex of the i-th edge
            if check[y] == False:
                check[y] = True
                q.append(y)

# dfs(start)
# print()
# bfs(start)
# print()

print(edges)
print(check)
print(cnt)

#acmicpc 1260
#input example:
# 4 5 1 (number of vertices, edges, and starting vertex)
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4