# 1. 전체 칸 순회하면서 방문하지 않은 땅이 있으면. bfs해서 섬 번호를 마킹 (이 과정이 끝나면 각각의 섬은 고유 번호를 가지게 됨)
# 2. 다시 순회하면서 해안(즉 육지와 인접한 0)을 발견하면 다리의 경로를 bfs(다른 섬을 발견하면 최소 길이 저장하고 종료)
from collections import deque
import sys
input=sys.stdin.readline
n = int(input())
country = [list(map(int, input().split())) for _ in range(n)]
moves = {(-1, 0), (0, 1), (1, 0), (0, -1)}

def markThisIsland(r, c, id_i):
    q = deque()
    q.append((r, c))
    country[r][c] = id_i
    while q:
        qr, qc = q.popleft()
        for dr, dc in moves:
            nr, nc = qr+dr, qc+dc
            if 0<=nr<n and 0<=nc<n and country[nr][nc] == 1:
                country[nr][nc] = id_i
                q.append((nr, nc))

id_island = 2
for r in range(n):
    for c in range(n):
        if country[r][c] == 1:
            markThisIsland(r, c, id_island)
            id_island += 1

min_bridge = n*2-3
def bfs(r, c, len_b, id_i):
    global min_bridge
    visited_bridge = [[0]*n for _ in range(n)]
    q = deque()
    q.append((r, c, len_b))
    visited_bridge[r][c] = 1

    while q:
        qr, qc, q_len_b = q.popleft()
        if q_len_b == min_bridge:
            return
        for dr, dc in moves:
            nr, nc = qr+dr, qc+dc
            if 0<=nr<n and 0<=nc<n:
                if country[nr][nc] == 0 and not visited_bridge[nr][nc]:
                    visited_bridge[nr][nc] = 1
                    q.append((nr, nc, q_len_b+1))
                elif country[nr][nc] != 0 and country[nr][nc] != id_i:
                    min_bridge = q_len_b
                    return

for r in range(n):
    for c in range(n):
        if country[r][c] == 0:
            already_bfsed = False
            for dr, dc in moves:
                if already_bfsed: continue
                nr, nc = r+dr, c+dc
                if 0<=nr<n and 0<=nc<n and country[nr][nc] != 0: # check if the sea is a coast
                    bfs(r, c, 1, country[nr][nc])
                    already_bfsed = True

print(min_bridge)