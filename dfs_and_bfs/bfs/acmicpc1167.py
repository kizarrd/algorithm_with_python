from collections import defaultdict, deque
import sys
input=sys.stdin.readline
V = int(input())
graph = defaultdict(list)
for _ in range(V):
    arr = list(map(int, input().split()))
    u = arr[0]
    i = 1
    while arr[i] != -1:
        graph[u].append((arr[i], arr[i+1]))
        graph[arr[i]].append((u, arr[i+1]))
        i += 2

def bfs(v_init):
    max_d = 0
    max_v = 0
    visited = [0]*(V+1)
    q = deque()
    q.append((v_init, 0))
    visited[v_init] = 1
    while q:
        v, d = q.popleft()
        if d > max_d:
            max_d = d
            max_v = v
        for adj_v, adj_d in graph[v]:
            if not visited[adj_v]:
                visited[adj_v] = 1
                q.append((adj_v, d+adj_d))
    return (max_v, max_d)

a1 = bfs(1)
a2 = bfs(a1[0])
print(a2[1])