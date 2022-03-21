import sys

def dfs(x, y):
    global board, R, C
    max_depth = 0
    queue = set()
    queue.add((x, y, board[y][x]))
    while queue:
        current_x, current_y, current_visited = queue.pop()
        max_depth = max(max_depth, len(current_visited))
        if max_depth == 26:
            return 26
        for movement in movement_array:
            next_x = current_x + movement[0]
            next_y = current_y + movement[1]
            if 0 <= next_x < C and 0 <= next_y < R and board[next_y][next_x] not in current_visited:
                queue.add((next_x, next_y, current_visited + board[next_y][next_x]))

    return max_depth


R, C = map(int, sys.stdin.readline().split())
board = []
for _ in range(R):
    row = list(sys.stdin.readline().strip())
    board.append(row)

movement_array = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]
start = (0, 0)
print(dfs(*start))
