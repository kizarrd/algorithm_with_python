import sys
input=sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

moves = ((0, 1), (1, 0))

dp[0][0] = 1

for r in range(N):
    for c in range(N):
        if r<N-1 or c<N-1:
            for dir_r, dir_c in moves:
                dr, dc = board[r][c]*dir_r, board[r][c]*dir_c
                nr, nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<N:
                    dp[nr][nc] += dp[r][c]

print(dp[N-1][N-1])