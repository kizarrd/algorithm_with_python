import sys
input=sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    d = [[0]*n for _ in range(2)] # d[r][c] = max score when including sticker(r, c)
    d[0][0] = stickers[0][0]
    d[1][0] = stickers[1][0]
    if n == 1:
        print(max(d[0][0], d[1][0]))
        continue
    d[0][1] = d[1][0]+stickers[0][1]
    d[1][1] = d[0][0]+stickers[1][1]
    if n == 2:
        print(max(d[0][1], d[1][1]))
    else:
        for i in range(2, n):
            d[0][i] = max(d[1][i-1]+stickers[0][i], d[1][i-2]+stickers[0][i])
            d[1][i] = max(d[0][i-1]+stickers[1][i], d[0][i-2]+stickers[1][i])
        print(max(d[0][n-1], d[1][n-1]))