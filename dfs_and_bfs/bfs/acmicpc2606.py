from collections import defaultdict, deque
import sys
input=sys.stdin.readline
V = int(input()) # Vertex
E = int(input()) # Edge

adj_list = defaultdict(list)
for _ in range(E):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(n):
    q = deque()
    visited = [0]*(V+1)
    q.append(n)
    visited[n] = 1

    cnt = 0
    while q:
        v = q.popleft()
        for adj_v in adj_list[v]:
            if not visited[adj_v]:
                visited[adj_v] = 1
                cnt += 1
                q.append(adj_v)

    return cnt

print(bfs(1))