N = int(input())
board = [list(input()) for _ in range(N)]

def count_longest_column(candy, c):
    r = 0
    local_max_cnt = 0
    while r < N:
        if board[r][c] == candy:
            cnt = 1
            r += 1
            while r < N and board[r][c] == candy:
                r += 1
                cnt += 1
            local_max_cnt = max(local_max_cnt, cnt)
        else:
            r += 1
    return local_max_cnt

def count_longest_row(candy, r):
    c = 0
    local_max_cnt = 0
    while c < N:
        if board[r][c] == candy:
            cnt = 1
            c += 1
            while c < N and board[r][c] == candy:
                c += 1
                cnt += 1
            local_max_cnt = max(local_max_cnt, cnt)
        else:
            c += 1
    return local_max_cnt

max_cnt = 0

for r in range(N):
    for c in range(N):
        if c < N-1:
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
            max_cnt = max(max_cnt, count_longest_column(board[r][c], c), count_longest_column(board[r][c+1], c+1), count_longest_row(board[r][c], r), count_longest_row(board[r][c+1], r))
            board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
        if r < N-1:
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
            max_cnt = max(max_cnt, count_longest_row(board[r][c], r), count_longest_row(board[r+1][c], r+1), count_longest_column(board[r][c], c), count_longest_column(board[r+1][c], c))
            board[r][c], board[r+1][c] = board[r+1][c], board[r][c]

print(max_cnt)