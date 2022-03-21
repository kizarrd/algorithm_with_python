from collections import deque
import sys
input=sys.stdin.readline
M, N, H = map(int, input().split())
boxes = []
for _ in range(H):
    boxes.append([list(map(int, input().split())) for _ in range(N)])

q = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if boxes[h][r][c] == 1:
                q.append((h, r, c, 0))

moves = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)] # dh, dr, dc
days = 0
while q:
    h, r, c, d = q.popleft()
    days = d
    for dh, dr, dc in moves:
        nh, nr, nc = h+dh, r+dr, c+dc
        if 0<=nh<H and 0<=nr<N and 0<=nc<M and boxes[nh][nr][nc] == 0:
            boxes[nh][nr][nc] = 1
            q.append((nh, nr, nc, d+1))

for h in range(H):
    for r in range(N):
        for c in range(M):
            if boxes[h][r][c] == 0:
                print(-1)
                exit()

print(days)