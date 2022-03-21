import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
def dfs(r, c):
    farmland[r][c] = 2
    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<M and farmland[nr][nc] == 1:
            dfs(nr, nc)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    farmland = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farmland[y][x] = 1
    
    cnt = 0
    for r in range(N):
        for c in range(M):
            if farmland[r][c] == 1:
                dfs(r, c)
                cnt += 1
    
    print(cnt)