N = int(input())
board = [list(input()) for _ in range(N)]

def count_longest_column(c):
    local_max_cnt = 0
    cnt = 1
    for r in range(1, N):
        if board[r][c] == board[r-1][c]:
            cnt += 1
            local_max_cnt = max(local_max_cnt, cnt)
        else:
            cnt = 1
    return local_max_cnt

def count_longest_row(r):
    local_max_cnt = 0
    cnt = 1
    for c in range(1, N):
        if board[r][c] == board[r][c-1]:
            cnt += 1
            local_max_cnt = max(local_max_cnt, cnt)
        else:
            cnt = 1
    return local_max_cnt

max_cnt = 0
for r in range(N):
    max_cnt = max(max_cnt, count_longest_row(r))
for c in range(N):
    max_cnt = max(max_cnt, count_longest_column(c))

for r in range(N):
    for c in range(N):
        if c < N-1 and board[r][c] != board[r][c+1]:
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
            max_cnt = max(max_cnt, count_longest_column(c), count_longest_column(c+1), count_longest_row(r))
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
        if r < N-1 and board[r][c] != board[r+1][c]:
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
            max_cnt = max(max_cnt, count_longest_row(r), count_longest_row(r+1), count_longest_column(c))
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c]

print(max_cnt)