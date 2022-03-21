from collections import defaultdict, deque
import sys
input=sys.stdin.readline

N, M, V = map(int, input().split())
adj_list = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

for key in adj_list:
    adj_list[key].sort()


visited = [0]*(N+1)
answers_dfs = []
def dfs(v):
    answers_dfs.append(v)
    visited[v] = 1
    for adj_v in adj_list[v]:
        if not visited[adj_v]:
            dfs(adj_v)

dfs(V)

visited = [0]*(N+1)
visited[V] = 1
answers_bfs = []
q = deque([V])
while q:
    v = q.popleft()
    answers_bfs.append(v)
    for adj_v in adj_list[v]:
        if not visited[adj_v]:
            visited[adj_v] = 1
            q.append(adj_v)

print(*answers_dfs)
print(*answers_bfs)