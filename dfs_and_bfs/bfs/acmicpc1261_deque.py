# dijkstra's algorithm
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(M)]

dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

dist = {}
dq = deque()
dq.appendleft((0, (0, 0)))

while dq:
    d, v = dq.popleft()
    c, r = v
    if (c, r) not in dist:
        dist[(c, r)] = d
        for i in range(4):
            nc = dc[i]+c
            nr = dr[i]+r
            if 0 <= nc < N and 0 <= nr < M:
                if graph[nr][nc] == 0:
                    dq.appendleft((d, (nc, nr)))
                elif graph[nr][nc] == 1:
                    dq.append((d+1, (nc, nr)))

print(dist[(N-1, M-1)])