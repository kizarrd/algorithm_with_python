import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

M, N = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)] # dp[r][c] = (r, c)에서 (M-1, N-1)까지 가는 경로의 수. 즉 우리가 찾는 답은 dp[0][0]. -1은 아직 계산되지 않았음을 뜻함.
moves = ((-1, 0), (0, 1), (1, 0), (0, -1))

def dfs(r, c): # dfs(r, c) 는 (r, c)에서 도착지점(M-1, N-1)까지 가는 경로의 수를 리턴하는 함수이다.
    if r == M-1 and c == N-1:
        return 1
    
    if dp[r][c] == -1: # (r, c)에서 도착지점까지 가는 경로의 개수가 아직 계산되지 않았다면, 계산.
        dp[r][c] = 0 # 이제 한번 계산한 지역은 최소 0을 리턴하게 됨.
        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0<=nr<M and 0<=nc<N and _map[nr][nc] < _map[r][c]:
                dp[r][c] += dfs(nr, nc)

    # 새로 계산했던, 이미 계산되어 있었던, 어쨌든 dp[r][c]를 리턴.
    return dp[r][c]

print(dfs(0, 0))