from collections import defaultdict
from heapq import heappush, heappop
import sys
input=sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

adj_list = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

dist = defaultdict(int)
hq = [(0, K)]
while hq:
    w, v = heappop(hq)
    if v not in dist:
        dist[v] = w
        for adj_v, adj_w in adj_list[v]:
            heappush(hq, (w + adj_w, adj_v))

for i in range(1, V+1):
    if i in dist:
        print(dist[i])
    else:
        print('INF')