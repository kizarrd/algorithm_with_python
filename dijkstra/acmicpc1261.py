# dijkstra's algorithm
from heapq import heappush, heappop

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(M)]

dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

dist = {}
pq = []
heappush(pq, (0, (0, 0))) # (dist, (c, r))

while pq:
    d, v = heappop(pq)
    c, r = v
    if (c, r) not in dist:
        dist[(c, r)] = d
        for i in range(4):
            nc = dc[i]+c
            nr = dr[i]+r
            if 0 <= nc < N and 0 <= nr < M:
                heappush(pq, (d+graph[nr][nc], (nc, nr)))

print(dist[(N-1, M-1)])