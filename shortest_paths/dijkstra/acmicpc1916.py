from heapq import heappush, heappop
import sys
input=sys.stdin.readline

N, M = int(input()), int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((w, v))

A, B = map(int, input().split())

dist = [-1 for _ in range(N+1)]
hq = [(0, A)]
while hq:
    w, v = heappop(hq)
    if dist[v] == -1:
        dist[v] = w
        for adj_w, adj_v in adj_list[v]:
            heappush(hq, (adj_w+w, adj_v))

print(dist[B])