from heapq import heappush, heappop
import sys
input=sys.stdin.readline

N, M, X = map(int, input().split())
adj_list = [[] for _ in range(M+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

going_back_to = [-1 for _ in range(N+1)]
hq = [(0, X)]
while hq:
    w, v = heappop(hq)
    if going_back_to[v] == -1:
        going_back_to[v] = w
        for adj_v, adj_w in adj_list[v]:
            heappush(hq, (adj_w+w, adj_v))

def dijkstra(start):
    dist = [-1 for _ in range(N+1)]
    hq = [(0, start)]
    while hq:
        w, v = heappop(hq)
        if dist[v] == -1:
            dist[v] = w
            if v == X: return w
            for adj_v, adj_w in adj_list[v]:
                heappush(hq, (adj_w+w, adj_v))
    return -1

_max = 0
for i in range(1, N+1):
    time_to_X = dijkstra(i)
    _max = max(_max, time_to_X + going_back_to[i])

print(_max)