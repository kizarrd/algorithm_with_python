N = int(input())
board = [[0]*N for _ in range(N)]
diagonal_moves = [(-1, -1), (-1, 1)]

def placeable(r, c):
    for dr, dc in diagonal_moves:
        nr, nc = r+dr, c+dc
        while 0<=nr<N and 0<=nc<N:
            if board[nr][nc]:
                return False
            nr, nc = nr+dr, nc+dc
    return True

cnt = 0
def dfs(r):
    global cnt
    if r==N:
        cnt += 1
        return
    for c in list(S):
        if placeable(r, c):
            board[r][c] = 1
            S.remove(c)
            dfs(r+1)
            S.add(c)
            board[r][c] = 0

S = set(i for i in range(N))
dfs(0)

print(cnt)