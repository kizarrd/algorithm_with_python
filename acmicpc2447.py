N = int(input())
pattern = [['*']*N for _ in range(N)]

def dc(r, c, n):
    if n == 1: 
        return
    n_div_3 = n//3

    for nr in range(r, r+n_div_3*2+1, n_div_3):
        for nc in range(c, c+n_div_3*2+1, n_div_3):
            if nr == r+n_div_3 and nc == c+n_div_3:
                continue
            dc(nr, nc, n_div_3)

    for i in range(r+n_div_3, r+n_div_3*2):
        for j in range(c+n_div_3, c+n_div_3*2):
            pattern[i][j]=' '

dc(0, 0, N)
for row in pattern:
    print(''.join(row))