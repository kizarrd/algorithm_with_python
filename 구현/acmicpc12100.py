from copy import deepcopy
from itertools import product

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
board_default = deepcopy(board)

paths = product([0, 1, 2, 3], repeat=5)

def move_and_merge(dir):
    if dir == 0:
        for c in range(N):
            not_merged = True
            for r in range(N):
                if board[r][c]:
                    prev = r
                    nr = r-1
                    while 0<=nr:
                        if board[nr][c] == 0:
                            board[nr][c], board[prev][c] = board[prev][c], board[nr][c]
                            nr -= 1
                            prev -= 1
                        elif board[nr][c] == board[prev][c] and not_merged:
                            board[prev][c], board[nr][c] = 0, board[nr][c]*2
                            not_merged = False
                            break
                        else:
                            break
    if dir == 1:
        for r in range(N):
            not_merged = True
            for c in range(N-1, -1, -1):
                if board[r][c]:
                    prev = c
                    nc = c+1
                    while nc<N:
                        if board[r][nc] == 0:
                            board[r][nc], board[r][prev] = board[r][prev], board[r][nc]
                            nc += 1
                            prev += 1
                        elif board[r][nc] == board[r][prev] and not_merged:
                            board[r][prev], board[r][nc] = 0, board[r][nc]*2
                            not_merged = False
                            break
                        else:
                            break
    if dir == 2:
        for c in range(N):
            not_merged = True
            for r in range(N-1, -1, -1):
                if board[r][c]:
                    prev = r
                    nr = r+1
                    while nr<N:
                        if board[nr][c] == 0:
                            board[nr][c], board[prev][c] = board[prev][c], board[nr][c]
                            nr += 1
                            prev += 1
                        elif board[nr][c] == board[prev][c] and not_merged:
                            board[prev][c], board[nr][c] = 0, board[nr][c]*2
                            not_merged = False
                            break
                        else:
                            break
    if dir == 3:
        for r in range(N):
            not_merged = True
            for c in range(N):
                if board[r][c]:
                    prev = c
                    nc = c-1
                    while 0<=nc:
                        if board[r][nc] == 0:
                            board[r][nc], board[r][prev] = board[r][prev], board[r][nc]
                            nc -= 1
                            prev -= 1
                        elif board[r][nc] == board[r][prev] and not_merged:
                            board[r][prev], board[r][nc] = 0, board[r][nc]*2
                            not_merged = False
                            break
                        else:
                            break
    # for row in board:
    #     print(*row)
    # print()
_max = 0

# path = [1, 2, 3, 2]
# print()
# for direction in path:
#     move_and_merge(direction)

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

'''
64 4 128
8  0  8
64 0  0

'''