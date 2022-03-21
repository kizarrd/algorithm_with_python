from heapq import heappush, heappop
import math
import sys
input=sys.stdin.readline

N, E = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((c, b))
    adj_list[b].append((c, a))
v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [math.inf for _ in range(N+1)]
    hq = [(0, start)]
    dist[start] = 0
    while hq:
        w, v = heappop(hq)
        if dist[v] < w:
            continue
        for adj_w, adj_v in adj_list[v]:
            alt = adj_w+w
            if alt < dist[adj_v]:
                dist[adj_v] = alt
                heappush(hq, (alt, adj_v))

    return dist

dist_from_1, dist_from_v1, dist_from_v2 = dijkstra(1), dijkstra(v1), dijkstra(v2)

distance1 = sum([dist_from_1[v1], dist_from_v1[v2], dist_from_v2[N]])
distance2 = sum([dist_from_1[v2], dist_from_v2[v1], dist_from_v1[N]])

print(min(distance1, distance2) if distance1!=math.inf or distance2!=math.inf else -1)