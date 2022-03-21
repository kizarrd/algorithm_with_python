import sys
input=sys.stdin.readline
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visited = set()
_max = 1

def dfs(r, c, d):
    global _max
    _max = max(_max, d)
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<R and 0<=nc<C and board[nr][nc] not in visited:
                visited.add(board[nr][nc])
                dfs(nr, nc, d+1)
                visited.remove(board[nr][nc])

visited.add(board[0][0])
dfs(0, 0, 1)
print(_max)