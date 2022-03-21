import sys
input=sys.stdin.readline
N = int(input())
video = [list(map(int, list(input().rstrip()))) for _ in range(N)]

def allSame(r, c, vlen):
    val = video[r][c]
    for i in range(r, r+vlen):
        for j in range(c, c+vlen):
            if video[i][j] != val:
                return False
    return True

def dc(r, c, vlen):
    if allSame(r, c, vlen):
        print(video[r][c], end='')
    else:
        print('(', end='')
        n_vlen = vlen//2
        dc(r, c, n_vlen)
        dc(r, c+n_vlen, n_vlen)
        dc(r+n_vlen, c, n_vlen)
        dc(r+n_vlen, c+n_vlen, n_vlen)
        print(')', end='')

dc(0, 0, N)