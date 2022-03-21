from collections import deque
import sys
input=sys.stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

q = deque()
for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            q.append((r, c, 0))

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
days = None
while q:
    r, c, days = q.popleft()
    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<M and graph[nr][nc] == 0:
            graph[nr][nc] = 1
            q.append((nr, nc, days+1))
# check if all ripe
for row in graph:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit()

print(days)