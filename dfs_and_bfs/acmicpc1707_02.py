from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
K = int(input())

def bfs(v_init):
    q = deque()
    q.append(v_init)
    groups[v_init] = 1
    while q:
        v = q.popleft()
        for adj_v in graph[v]:
            if groups[v] == groups[adj_v]:
                return False
            elif groups[adj_v] == 0:
                groups[adj_v] = -groups[v]
                q.append(adj_v)
    return True

for _ in range(K):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    yes = True
    groups = [0]*(V+1)
    for v in range(1, V+1):
        if not groups[v]:
            yes = bfs(v)
            if not yes:
                break
    if yes:
        print('YES')
    else:
        print('NO')