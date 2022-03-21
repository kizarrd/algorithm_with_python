from heapq import heappush, heappop
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

moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
def get_eatable_fish_bfs(sr, sc):
    pq = []
    heappush(pq, (0, sr, sc))
    visited = [[0]*N for _ in range(N)]
    visited[sr][sc] = 1
    while pq:
        d, r, c = heappop(pq)
        if 0 < sea[r][c] < sharkSize:
            return (r, c, d)
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                if sea[nr][nc] <= sharkSize:
                    visited[nr][nc] = 1
                    heappush(pq, (d+1, nr, nc))
    return 0

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