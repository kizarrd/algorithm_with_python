from collections import deque
n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)]
check = [False] * (n+1)
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(n):
    a[i].sort()

print(a)
print(check)

#input example:
# 4 5 1 (number of vertices, edges, and starting vertex)
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# starting vertex will be used when dfs or bfs is used.