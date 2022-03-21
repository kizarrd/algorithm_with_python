# Time Limit Exceeded
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
visited[0][0] = True
moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
directions = ('U', 'R', 'D', 'L')

h_max = 0
p_max = ''
def dfs(r, c, h, p): # row, column, happiness, direction, path
    global h_max, p_max
    print(p)
    if r == R-1 and c == C-1:
        if h > h_max:
            h_max = h
            p_max = p
        return
    for i in range(4):
        dr, dc = moves[i]
        nr, nc = r+dr, c+dc
        if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, h+graph[nr][nc], p+directions[i])
            visited[nr][nc] = False

dfs(0, 0, graph[0][0], '')
print(p_max)