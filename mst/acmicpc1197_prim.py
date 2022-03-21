# prim's
from heapq import heappush, heappop
import sys
input=sys.stdin.readline

V, E = map(int, input().split())
adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((w, v))
    adj_list[v].append((w, u))

hq = [(0, 1)] # (w, start)
visited = [0]*(V+1)
weights = 0
cnt = 0
while hq:
    w, v = heappop(hq)
    if not visited[v]:
        visited[v] = 1
        weights += w
        cnt += 1
        if cnt == V:
            break
        for adj_w, adj_v in adj_list[v]:
            if not visited[adj_v]:
                heappush(hq, (adj_w, adj_v))

print(weights)