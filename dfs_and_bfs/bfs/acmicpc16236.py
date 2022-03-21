from collections import deque
import sys
input=sys.stdin.readline
N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
sharkSize = 2

babyShark_location = [0, 0]
for r in range(N):
    if 9 in sea[r]:
        babyShark_location = [r, sea[r].index(9)]
        sea[babyShark_location[0]][babyShark_location[1]] = 0
        break

moves = [(-1, 0), (0, -1), (0, 1), (1, 0)] # up first, left second
def get_eatable_fish_bfs(sr, sc):
    q = deque()
    q.append((sr, sc, 0)) # r, c, distance
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1
    eatable = []
    while q:
        r, c, d = q.popleft()
        if eatable:
            if eatable[-1][-1] == d:
                continue
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if 0 < sea[nr][nc] < sharkSize: # if eatable
                    eatable.append((nr, nc, d+1))
                elif sea[nr][nc] > sharkSize:
                    continue
                else:
                    visited[nr][nc] = 1
                    q.append((nr, nc, d+1))

    eatable.sort(key=lambda x: (x[0], x[1]))
    return eatable[0] if eatable else 0

time = 0
eaten = 0
while True:
    fish = get_eatable_fish_bfs(babyShark_location[0], babyShark_location[1])
    if not fish:
        break
    # count time
    time += fish[2]
    # update shark location, update map(eat fish)
    babyShark_location[0], babyShark_location[1] = fish[0], fish[1]
    sea[fish[0]][fish[1]] = 0
    # update shark size
    eaten += 1
    if eaten == sharkSize:
        sharkSize += 1
        eaten = 0

print(time)