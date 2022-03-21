R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
moves = ((-1, 0), (0, 1), (1, 0), (0, -1))
visited = {}
answers = []

def dfs(r, c, d):
    immovable = True
    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        if 0<=nr<R and 0<=nc<C:
            if board[nr][nc] not in visited or not visited[board[nr][nc]]:
                immovable = False
                visited[board[nr][nc]] = True
                dfs(nr, nc, d+1)
                visited[board[nr][nc]] = False
    if immovable:
        answers.append(d)

visited[board[0][0]] = True
dfs(0, 0, 1)
print(max(answers))