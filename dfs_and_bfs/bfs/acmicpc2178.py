from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1] # c: column, r: row
visited = [[False]*M for _ in range(N)]
q = deque()
q.append((0, 0, 1)) #(r, c, distance)
while q:
    r, c, dist = q.popleft()
    if r == N-1 and c == M-1:
        print(dist)
        break
    if not visited[r][c]:
        visited[r][c] = True
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if -1 < nr < N and -1 < nc < M and graph[nr][nc]:
                q.append((nr, nc, dist+1))