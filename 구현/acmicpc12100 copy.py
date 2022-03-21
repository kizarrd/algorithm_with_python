from itertools import product

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
board_default = []
for i in range(N):
    board_default.append(board[i][:])

paths = product([0, 1, 2, 3], repeat=5)

def move_and_merge(dir):
    if dir == 0:
        for c in range(N):
            prev = 0
            for r in range(1, N):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[prev][c] == 0:
                        board[prev][c] = temp
                    elif board[prev][c] == temp:
                        board[prev][c] = temp*2
                        prev += 1
                    else:
                        prev += 1
                        board[prev][c] = temp
    elif dir == 1:
        for r in range(N):
            prev = N-1
            for c in range(N-2, -1, -1):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[r][prev] == 0:
                        board[r][prev] = temp
                    elif board[r][prev] == temp:
                        board[r][prev] = temp*2
                        prev -= 1
                    else:
                        prev -= 1
                        board[r][prev] = temp     
    elif dir == 2:
        for c in range(N):
            prev = N-1
            for r in range(N-2, -1, -1):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[prev][c] == 0:
                        board[prev][c] = temp
                    elif board[prev][c] == temp:
                        board[prev][c] = temp*2
                        prev -= 1
                    else:
                        prev -= 1
                        board[prev][c] = temp    
    elif dir == 3:
        for r in range(N):
            prev = 0
            for c in range(1, N):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[r][prev] == 0:
                        board[r][prev] = temp
                    elif board[r][prev] == temp:
                        board[r][prev] = temp*2
                        prev += 1
                    else:
                        prev += 1
                        board[r][prev] = temp

_max = 0
for path in paths:
    for direction in path:
        move_and_merge(direction)
    # get_max
    path_max = max(list(map(max, board)))
    _max = max(_max, path_max)
    # reset board
    for i in range(N):
        board[i] = board_default[i][:]

print(_max)