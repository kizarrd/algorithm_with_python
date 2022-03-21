import sys
input=sys.stdin.readline

R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    row = list(sys.stdin.readline().strip())
    board.append(row)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r_init, c_init, visited_init):
    _max = 1
    stack = set()
    stack.add((r_init, c_init, visited_init))
    while stack:
        r, c, current_visited = stack.pop()
        _max = max(_max, len(current_visited))
        if _max == 26:
            return 26
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            
            if 0<=nr<R and 0<=nc<C and board[nr][nc] not in current_visited:
                stack.add((nr, nc, current_visited+board[nr][nc]))
    return _max

print(dfs(0, 0, board[0][0]))