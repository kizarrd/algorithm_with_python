'''
ㅡ, ㅣ (blue)
ㅁ  (yellow)
ㄴ*4*2 (orange)
ㄴㄱ*2*2 (green)
ㅜ,ㅓ,ㅗ,ㅏ (pink)
==> 2+1+8+4+4 = 19
'''
import sys
input=sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
max_val = max(map(max, paper))
max_sum = 0
moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
def dfs(r, c, d, _sum):
    global max_sum
    if _sum + max_val*(4-d) < max_sum:
        return
    if d == 4:
        max_sum = max(max_sum, _sum)
        return
    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
            visited[nr][nc] = 1
            if d == 2: # condition for pink shape
                dfs(r, c, d+1, _sum+paper[nr][nc])
            dfs(nr, nc, d+1, _sum+paper[nr][nc])
            visited[nr][nc] = 0

visited = [[0]*M for _ in range(N)]
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 1, paper[r][c])
        visited[r][c] = 0

print(max_sum)